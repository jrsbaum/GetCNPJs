from req_api import CNPJCollector, GetError
from db import collection, collection2


class CNPJInputValidation:
    @staticmethod
    def user_input():
        qual_api = input("Em qual API voce gostaria de consultar? 1 ou 2? ")
        match qual_api:
            case "1":
                cnpjs = input("Digite os CNPJs separados por vírgula: ")
                cnpjs = cnpjs.split(",")
                for cnpj in cnpjs:
                    try:
                        data = CNPJCollector.get_cnpj_api_1(cnpj)
                        collection.insert_one(data)
                        print(f"Dados inseridos no banco de dados para o CNPJ {cnpj}.")
                    except Exception as e:
                        GetError.get_log_if_error(cnpj, e)
                        print(f"Erro ao obter dados para o CNPJ {cnpj}: {e}")
            case "2":
                cnpjs = input("Digite os CNPJs separados por vírgula: ")
                cnpjs = cnpjs.split(",")
                for cnpj in cnpjs:
                    try:
                        token = CNPJCollector.get_cnpj_token()
                        data = CNPJCollector.get_cnpj_api_2(cnpj, token)
                        print(f"Dados obtidos com sucesso para o CNPJ {cnpj}!")
                        collection2.insert_one(data)
                        print(f"Dados inseridos no banco de dados para o CNPJ {cnpj}.")
                    except Exception as e:
                        print(f"Erro ao obter dados para o CNPJ {cnpj}: {e}")

