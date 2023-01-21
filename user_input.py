from req_api import get_cnpj
from db import collection


class InputOptions:
    def user_input(self):
        cnpjs = input("Digite os CNPJs separados por vírgula: ")
        cnpjs = cnpjs.split(",")
        for cnpj in cnpjs:
            try:
                data = get_cnpj(cnpj)
                print(f"Dados obtidos com sucesso para o CNPJ {cnpj}!")
                collection.insert_one(data)
                print(f"Dados inseridos no banco de dados para o CNPJ {cnpj}.")
            except Exception as e:
                print(f"Erro ao obter dados para o CNPJ {cnpj}: {e}")
