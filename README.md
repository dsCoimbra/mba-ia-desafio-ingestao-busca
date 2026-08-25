# Desafio MBA Engenharia de Software com IA - Full Cycle


>*Você deve entregar um software capaz de:
**1. Ingestão**: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector.
**2. Busca**: Permitir que o usuário faça perguntas via linha de comando (CLI) e receba respostas baseadas apenas no conteúdo do PDF.*
___

### Requisitos para o projeto:

- Api Key OpenAI
- Python 3.13
___
#### Configuração do projeto:

##### Criando o ambiente virtual
```sh
python3 -m venv venv
```

##### Instalando as dependencias
```sh
pip install -r requirements.txt
```

##### Iniciando o ambiente virtual
```sh
source venv/bin/activate
```

##### Criando banco 
```sh
docker compose up -d
```
___

#### Comandos para rodar o projeto

##### Ingestão de documentos
```sh
python src/ingest.py
```

##### Ativar modo chat
```sh
python src/chat.py
```
