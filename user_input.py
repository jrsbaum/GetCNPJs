from req_api import get_cnpj_api_1, GetError, get_cnpj_api_2
from db import collection


class CNPJInputValidation:
    @staticmethod
    def user_input():
        cnpjs = input("Digite os CNPJs separados por vírgula: ")
        cnpjs = cnpjs.split(",")
        for cnpj in cnpjs:
            try:
                qual_api = input("Em qual API voce gostaria de consultar? 1 ou 2? ")
                match qual_api:
                    case "1":
                        data = get_cnpj_api_1(cnpj)
                        collection.insert_one(data)
                        print(f"Dados inseridos no banco de dados para o CNPJ {cnpj}.")
                    case "2":
                        data = get_cnpj_api_2(cnpj)
                        print(f"Dados obtidos com sucesso para o CNPJ {cnpj}!")
                        collection.insert_one(data)
                        print(f"Dados inseridos no banco de dados para o CNPJ {cnpj}.")

            except Exception as e:
                GetError.get_log_if_error(cnpj, e)
                print(f"Erro ao obter dados para o CNPJ {cnpj}: {e}")
