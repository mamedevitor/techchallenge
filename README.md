# Projeto API Embrapa - Tech Challenge MLE1

### Criadores: Rubens Pinheiro | Vitor Mamede | Vitor Perencine
### Grupo 20

## Objetivo

Este projeto foi desenvolvido para suprir a necessidade de criar uma API que permita consultas públicas aos dados disponíveis no site da Embrapa do Rio Grande do Sul.

Os dados podem ser acessados através do site da Embrapa no endereço http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01.

Nesse site, é possível consultar e filtrar os dados por ano, com diferentes tipos de consultas organizadas nas abas produção, processamento, comercialização, importação e exportação. Cada aba oferece a opção de baixar os arquivos em formato CSV, contendo os dados específicos daquela categoria.

A finalidade deste projeto é disponibilizar uma API que permita o acesso a esses dados, possibilitando que sejam utilizados em processos automatizados para a criação de um banco de dados. Esse banco de dados poderá então servir como base para análises utilizando modelos de machine learning.


## Descrição da API:

Esta API foi desenvolvida em Python, utilizando o framework FastAPI.

A carga dos dados ocorre durante a execução da API, onde é realizado um processo de scraping no site da Embrapa. Esse processo busca todos os links de download dos arquivos CSV e gera uma lista deles, incluindo a referência da aba em que estão localizados no site da Embrapa.

Posteriormente, a API baixa cada um desses arquivos, cria um banco de dados local, processa os arquivos e os armazena no banco de dados.

Optou-se pelo SQLite como banco de dados devido à sua praticidade, já que não requer instalação ou configuração, além de ser adequado para o volume de dados relativamente pequeno que será tratado. Além disso, o projeto não será submetido a uma alta carga de consultas simultâneas, pois lida com dados históricos que são atualizados com pouca frequência.

## Repositório da API no github

https://github.com/mamedevitor/techchallenge  
<br/>
 <br/>

## Endpoints disponibilizados
Devem ser chamados com requisições GET, a fim de se obter os dados desejados. Segue a relação de dados desejados e endpoints:

Auth : /token/

Produção: /producao/

Processamento de Viníferas: /processa_viniferas/

Processamento de Americanas e Hídridas: /processa_americanas_hibridas/

Processamento de Uvas de Mesa: /processa_uvamesa/

Processamento Sem Classificação: /processa_semclassf/

Comercialização: /comercio/

Importação de Vinhos de Mesa: /importacao_vinhos/

Importação de Espumantes: /importacao_espumantes/

Importação de Uvas Frescas: /importacao_uvasfrescas/

Importação de Uvas Passas: /importacao_uvaspassas/

Importação de Suco de Uva: /importacao_suco/

Exportação de Vinhos de Mesa: /exportacao_vinhosmesa/

Exportação de Espumantes: /exportacao_espumantes/

Exportação de Uvas Frescas: /exportacao_uvasfrescas/

Exportação de Suco de Uva: /exportacao_suco/

## Autenticação

Antes de utilizar a API, deve-se chamar o endpoint /token com requisição POST para se obter um token JWT, enviando os parâmetros "username" e "password". Segue exemplo de request em Bash, considerando que se deve substituir SEU_USER pelo usuário e SUA_SENHA pela senha:

![image](https://github.com/mamedevitor/techchallenge/assets/55901404/ce89c34b-30da-4014-980d-f0c4bc4d4f18)

Modelo da response:

![image](https://github.com/mamedevitor/techchallenge/assets/55901404/1ae943b6-6dbc-47cd-a10f-7ef99e11dd01)

## Requisição

As requisições precisam incluir os parâmetros skip (Número de registros a serem pulados (default: 0)) e limit (Número máximo de registros a serem retornados (default: 10)). Exemplo de request em bash:

![image](https://github.com/mamedevitor/techchallenge/assets/55901404/0e594932-319c-400f-bd67-5082e76031ba)

Todos retornam uma lista de dicionários, em que cada key é o título da coluna e o valor é o valor da linha. Exemplo de response:

![image](https://github.com/mamedevitor/techchallenge/assets/55901404/87c0f129-1ddb-4747-917c-f156f0e96c0d)

![image](https://github.com/mamedevitor/techchallenge/assets/55901404/dfcdbc31-2ede-439c-b765-30f44204143e)

# Processo de deploy da API

## Deploy no desktop

Após a replicação do repositório no ambiente de execução, basta seguir os passos listados abaixo:

#### Crie um ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
#### Rodando o projeto

```bash
uvicorn app.main:app --reload
```
 
## Deploy no Heroku

#### 1. Criar repositório no github:
```bash
git init
git add .
git commit -m "Initial commit"
```

#### 2. Crie um arquivo Procfile na raiz do projeto e dentro dele o seguinte código:
```bash
web: uvicorn app.main:app --host 0.0.0.0 --port ${PORT}
```

#### 3. Crie um novo aplicativo no Heroku:
```bash
heroku create vitibrasil-api
```
#### 4. Faça o deploy para o Heroku:
```bash
git push heroku master
```
#### 5. Escale a aplicação:
```bash
heroku ps:scale web=1
```

6. Acesse sua aplicação:
Heroku fornecerá um link para a aplicação. Acesse o link para ver sua API em funcionamento na nuvem.
https://api-tech-challenge-fiap-ba4acd78ab5d.herokuapp.com/docs

<br/>
<br/>
<br/>
<br/>

Licença

MIT Licence.
