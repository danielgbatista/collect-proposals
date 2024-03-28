import requests

def list(page):
    url = f"https://dadosabertos.camara.leg.br/api/v2/proposicoes?pagina={page}&itens=100&ordem=ASC&ordenarPor=id"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            result = response.json()
            data = result
            return data['dados'], response.status_code
        else:
            print("Erro ao acessar a API:", response.status_code)
            return None

    except Exception as error:
        print("Erro ao fazer requisição à API:", error)

def insert(listPropositions):
    url = f"https://dejur-server-dev.azurewebsites.net/api/v1/data-integration/legislative-proposals"
    try:
        response = requests.post(url, json = listPropositions)

        if response.status_code == 202:
            print("Tudo certo inserido com sucesso")
            return True
        else:
            print("Erro ao acessar a API:", response.status_code)
            return False

    except Exception as error:
        print("Erro ao fazer requisição à API:", error)