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
    print(response.text)
