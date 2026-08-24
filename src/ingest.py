import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()
for k in ("OPENAI_API_KEY", "DATABASE_URL", "PG_VECTOR_COLLECTION_NAME", "PDF_PATH"):
    if not os.getenv(k):
        raise RuntimeError(f"{k} is not set in the environment variables.")

def ingest_pdf():
    current_dir = Path(__file__).parent
    PDF_PATH = current_dir / os.getenv("PDF_PATH")

    loader = PyPDFLoader(str(PDF_PATH)).load()
    splits = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150, add_start_index=False).split_documents(loader)
    if not splits:
        raise SystemExit("No document splits were created.")

    documents = [Document(
        page_content=doc.page_content,
        metadata={k: v for k, v in doc.metadata.items() if v not in ("", None)}
    ) for doc in splits]

    ids = [i for i in range(len(documents))]

    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"))

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True
    )

    store.add_documents(documents=documents, ids=ids)

if __name__ == "__main__":
    ingest_pdf()