import json

from req_api import get_cnpj, get_next_page
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
                query_id = data['QueryId']
                print(query_id)

                # data_next = get_next_page(data, cnpj)
                testedocapeta = data['Result'][0]['Lawsuits']
                print(f"Adicionando novos itens")
                filters = {"QueryId": f"{query_id}"}
                newvalues = {"$set": {'DataFromNextPage: ': f"'Lawsuits': {testedocapeta}"}}
                # print(data_next)
                collection.update_one(filters, newvalues)
                print(f"Dados atualizados no banco de dados para o CNPJ {cnpj}.")

            except Exception as e:
                print(f"Erro ao obter dados para o CNPJ {cnpj}: {e}")

