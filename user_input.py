from req_api import get_cnpj


def user_input(cnpj):
    cnpj = input("Digite o CNPJ: ")
    get_cnpj(cnpj)