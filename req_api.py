import datetime
import os

import requests
import cfg


def get_cnpj(cnpj):
    url = cfg.url
    payload = {
        "Datasets": cfg.datasets,
        "q": f"doc{{{cnpj}}}",
        "Limit": 1
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "AccessToken": cfg.access_token
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        get_log_if_error(cnpj, response)
        raise Exception("Error while fetching data")
    return response.json()


def get_next_page(data, cnpj):
    teste = data['Result'][0]['Lawsuits']
    if 'NextPageId' not in teste:
        return print("nao ha nextpageid")
    next_page_id = teste['NextPageId']
    print(f"NextPageId: {next_page_id}")
    url = cfg.url
    payload = {
        "Datasets": f"processes.next({next_page_id})",
        "q": f"doc{{{cnpj}}}",
        "Limit": 1
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "AccessToken": cfg.access_token
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        get_log_if_error(cnpj, response)
        raise Exception("Error while fetching data")
    # chamada recursiva
    get_next_page(response.json(), cnpj)


def get_log_if_error(cnpj, response):
    # abrindo o arquivo para escrita
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    file_name = f"log{cnpj} {current_time}.txt"

    # Cria a pasta logs caso nao exista
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Salva o arquivo na pasta logs
    with open(f"logs/{file_name}", "w") as f:
        f.write(response.text)




