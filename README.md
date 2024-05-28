API Embrapa



Descrição:

API REST que realiza uma query no banco de dados local e retorna informações de vitivinicultura da Emprapa, incluindo dados de Produção, Processamento (de Viníferas, Americanas e Hídridas, Uvas de Mesa e Sem Classificação), Comercialização, Importação (de Vinhos de Mesa, Espumantes, Uvas Frescas, Uvas Passas e Suco de Uva) e Exportação (de Vinhos de Mesa, Espumantes, Uvas Frescas e Suco de Uva). A API não requer instalações adicionais.
Link principal da API: https://api-tech-challenge-fiap-ba4acd78ab5d.herokuapp.com




Autenticação

Antes de utilizar a API, deve-se chamar o endpoint /token com requisição POST para se obter um token JWT, enviando os parâmetros "username" e "password". Segue exemplo em Bash, considerando que se deve substituir SEU_USER pelo usuário e SUA_SENHA pela senha:


![image](https://github.com/mamedevitor/techchallenge/assets/55901404/ce89c34b-30da-4014-980d-f0c4bc4d4f18)

O retorno é no modelo:


![image](https://github.com/mamedevitor/techchallenge/assets/55901404/1ae943b6-6dbc-47cd-a10f-7ef99e11dd01)


Endpoints



Devem ser chamados com requisições GET, a fim de se obter os dados desejados. Segue a relação de dados desejados e endpoints:

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

Todos retornam (xpto)



Exemplos de uso

(desenvolver)



Licença

MIT Licence.
