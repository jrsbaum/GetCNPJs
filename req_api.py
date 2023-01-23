import requests
import cfg
from db import collection


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
        raise Exception("Error while fetching data")
    return response.json()


def get_next_page(data, cnpj):
    lawsuits = data['Result'][0]['Lawsuits']
    if 'NextPageId' not in lawsuits:
        return print("no next page id")
    next_page_id = lawsuits['NextPageId']
    print(f"NextPageId: {next_page_id}")
    url = cfg.url
    payload = {
        "Datasets": f"{cfg.datasets_next}({next_page_id})",
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
        raise Exception("Error while fetching data")

    query_id = data['QueryId']
    filters = {"QueryId": f"{query_id}"}
    newvalues = {"$set": {f'Continue': f"{lawsuits}"}}
    collection.update_one(filters, newvalues)
    get_next_page(response.json(), cnpj)
