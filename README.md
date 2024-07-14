# API Ecommerce OpenAI

Esta é uma API desenvolvida em Flask que integra o OpenAI para fornecer assistência em vendas de produtos para animais de estimação.

## Sumário

- [Características](#características)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Executando o Projeto](#executando-o-projeto)
- [Testes](#testes)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)

## Características

- Endpoint para análise de perguntas sobre produtos para animais de estimação.
- Utiliza a API do OpenAI para gerar respostas.
- Estrutura de código modular e testável.

## Tecnologias Utilizadas

- **Flask**: Framework para desenvolvimento web.
- **Flask-RESTx**: Extensão para construção de APIs RESTful.
- **OpenAI**: API para geração de texto.
- **Docker**: Contêineres para isolamento do ambiente.
- **pytest**: Framework para testes.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.7 ou superior
- Docker e Docker Compose

### Variáveis de Ambiente

Crie um arquivo `config.ini` na raiz do projeto com o seguinte conteúdo:

```ini
[openai]
OPENAI_KEY=your_openai_api_key
```

## Executando o Projeto

### Com Docker
Para executar a aplicação utilizando Docker, execute os seguintes comandos:

1. Construir os contêineres: 

```bash
docker-compose build
```

2. Iniciar a aplicação:

```bash
docker-compose up
```

A API estará disponível em http://localhost:5500/api/ecommerce/v1.

### Sem Docker
Para executar o projeto sem Docker, siga os passos abaixo:

1. Instalar dependências:

```bash
pip install -r requirements.txt
```

2. Executar a aplicação:

```bash
python run.py
```

## Testes
Para rodar os testes, use:

### Com Docker

```bash
docker-compose run test
```

Sem Docker
```bash
pytest
```

## Estrutura do Projeto

```bash
.
├── app
│   ├── main
│   │   ├── openai
│   │   │   ├── __init__.py
│   │   │   ├── openai_controller.py
│   │   │   ├── openai_response_models.py
│   │   │   └── openai_service.py
│   └── __init__.py
├── config.ini
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```