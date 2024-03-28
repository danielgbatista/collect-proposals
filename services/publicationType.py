import requests

def insert(type):
    url = f"https://dejur-server-dev.azurewebsites.net/api/v1/data-integration/publication-types"
    try:
        response = requests.post(url, json=type)

        if response.status_code == 202:
            print("Tudo certo inserido com sucesso")
            return True
        else:
            print("Erro ao acessar a API:", response.status_code)
            return False

    except Exception as error:
        print("Erro ao fazer requisição à API:", error)

def find(search):
    url = f"https://dejur-server-dev.azurewebsites.net/api/v1/publication-types"
    try:
        response = requests.get(url, params={ "search": search })

        if response.status_code == 200:
            result = response.json()
            data = result
            return data, response.status_code
        else:
            print("Erro ao acessar a API:", response.status_code)
            return None

    except Exception as error:
        print("Erro ao fazer requisição à API:", error)