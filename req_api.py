from datetime import datetime

import os
import requests
import cfg


def get_cnpj_api_1(cnpj):
    url = cfg.url
    payload = {
        "Datasets": cfg.datasets,
        "q": f"doc{{{cnpj}}}",
        "Limit": 1
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "AccessToken": cfg.access_token1
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception("Error while fetching data")
    print("passou")
    return response.json()


def get_cnpj_api_2(cnpj):
    url = cfg.url
    payload = {
        "Datasets": cfg.datasets,
        "q": f"doc{{{cnpj}}}",
        "Limit": 1
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "AccessToken": cfg.access_token2
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        GetError.get_log_if_error(cnpj, Exception)
        raise Exception("Erro ao buscar dados")
    print(f"Dados obtidos com sucesso para o CNPJ {cnpj}!")
    return response.json()


class GetError:
    @staticmethod
    def get_log_if_error(cnpj, e):
        # abrindo o arquivo para escrita
        current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        file_name = f"log{cnpj} {current_time}.txt"

        # Cria a pasta logs caso nao exista
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # Salva o arquivo na pasta logs
        with open(f"logs/{file_name}", "w") as f:
            f.write(e)
