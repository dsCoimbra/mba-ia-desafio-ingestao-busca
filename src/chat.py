from search import search_prompt

def main():
    while True:
        pergunta = input("Faça sua pergunta: \n")
        chain = search_prompt(pergunta)
    
        if not chain:
            print("Resposta: \nNão foi possível iniciar o chat. Verifique os erros de inicialização.")
            return
        
        print(f"Resposta: \n{chain}")
        print("="*50)

if __name__ == "__main__":
    main()