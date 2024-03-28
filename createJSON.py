import json

# insere linha por item
def insertRow(response, file):
    for item in response[0]:
        if item:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')
        else:
            return None

#cria arquivo
def insertJSON(response, fileName):
    # Cria arquivo e insere um objeto dentro pulando uma linha
    with open(fileName, "a") as file:
        insertRow(response, file)