import sys

from req_api import get_cnpj, get_next_page
from db import collection
import math


class InputOptions:
    @staticmethod
    def user_input():
        cnpjs = input("Digite os CNPJs separados por vírgula: ")
        cnpjs = cnpjs.split(",")
        for cnpj in cnpjs:
            try:
                data = get_cnpj(cnpj)
                data_size = sys.getsizeof(data)
                if data_size > 15000000:
                    # Calcular quantas partes são necessárias para dividir o documento
                    parts = math.ceil(data_size / 15000000)
                    for i in range(parts):
                        # Dividir o documento em partes de 15 MB
                        part = data[i * 15000000:(i + 1) * 15000000]
                        collection.insert_one(part)
                        print(f"Dados inseridos no banco de dados para o CNPJ {cnpj}.")
                else:
                    collection.insert_one(data)
                    print(f"Dados inseridos no banco de dados para o CNPJ {cnpj}.")

                get_next_page(data, cnpj)
                print(f"Dados atualizados no banco de dados para o CNPJ {cnpj}.")

            except Exception as e:
                print(f"Erro ao obter dados para o CNPJ {cnpj}: {e}")
