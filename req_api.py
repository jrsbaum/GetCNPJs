from datetime import datetime

import os
import requests
import cfg


class CNPJCollector:
    @staticmethod
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
            GetError.get_log_if_error(cnpj, Exception)
            raise Exception("Error while fetching data")
        return response.json()

    @staticmethod
    def get_cnpj_token():
        url = cfg.url2
        payload = {"application": cfg.application_id, "application_secret": cfg.application_id_secret}
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=payload, headers=headers)
        print(f"token?: {response.text}")
        data = response.json()
        token = data["token"]
        return token

    @staticmethod
    def get_cnpj_api_2(cnpj, token):
        url = f"{cfg.url_req}/{cnpj}"
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = requests.post(url, headers=headers)
        data = response.json()
        if response.status_code != 200:
            raise Exception("Erro ao buscar dados")
        print(f"Dados obtidos com sucesso para o CNPJ {cnpj}!")
        return data


class GetError:
    @staticmethod
    def get_log_if_error(cnpj, e):
        current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        file_name = f"log{cnpj} {current_time}.txt"

        if not os.path.exists("logs"):
            os.makedirs("logs")

        with open(f"logs/{file_name}", "w") as f:
            f.write(e)
