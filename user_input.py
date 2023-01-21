from req_api import get_cnpj
from db import Processes


class InputOptions:
    def user_input(self):
        cnpj = input("Digite o CNPJ: ")
        data = get_cnpj(cnpj)
        print("Dados obtidos com sucesso!")
        decision = input("Voce quer inserir essa info no banco de dados?? s/n: ")
        if decision == 's' or decision == 'S':
            Processes.insert_one(data)
            print("Dados inseridos no banco de dados.")
        else:
            print("Dados nao inseridos no banco de dados.")

