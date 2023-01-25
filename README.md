
## GetCNPJs

Este projeto é um script em Python que tem como objetivo buscar informações de empresas registradas no Brasil, através do seu CNPJ (Cadastro Nacional de Pessoa Jurídica).

Ele é composto por três arquivos principais: user_input.py, req_api.py e db.py.

```
     user_input.py
```
O arquivo user_input.py é responsável por gerenciar a entrada de dados do usuário. Ele permite que o usuário escolha entre duas APIs diferentes para buscar informações sobre CNPJs. O usuário pode digitar vários CNPJs separados por vírgulas e o script os trata individualmente. Ele também gerencia as exceções e erros que podem ocorrer durante o processo de busca de informações.

```
    req_api.py
```   
O arquivo req_api.py é responsável por fazer as requisições HTTP para as APIs escolhidas pelo usuário. Ele contém duas funções principais: get_cnpj_api_1 e get_cnpj_api_2, que são responsáveis por buscar informações sobre um CNPJ específico através de cada uma das APIs disponíveis. Ele também contém uma função chamada get_cnpj_token, que é usada para obter um token de autenticação necessário para utilizar a segunda API.

```
    db.py
```
O arquivo db.py é responsável por gerenciar a conexão com o banco de dados MongoDB e inserir as informações obtidas das APIs. Ele é responsável por inserir os dados obtidos para cada CNPJ em duas coleções diferentes no banco de dados e registrar os erros que podem ocorrer durante o processo de inserção.

---

#### Em resumo, o script "GetCNPJs" é uma ferramenta útil para coletar informações sobre empresas registradas no Brasil através do seu CNPJ, usando duas APIs diferentes e salvando essas informações em um banco de dados MongoDB. Ele também gerencia as exceções e erros que podem ocorrer durante o processo de busca de informações.

---
### Para o código funcionar, precisa de um arquivo cfg.py que não foi versionado. O arquivo contém o seguinte código:

```
mongo_client_key = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]"

url = "https://url-da-api"

database_name = "database_name"
collection_name = "collection_name"

access_token1 = "access_token"

datasets = "datasets"

# ------------------------------------ #

url2 = "https://url-da-api2/auth/token"
url_req = "https://url-da-api-2"


database_name2 = "database_name2"
collection_name2 = "collection_name2"

application_id = "application_id"
application_id_secret = "application_id_secret"


```

#### Substitua os valores pelos valores a serem usados.