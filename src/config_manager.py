import json

def carregar_config():
    with open("config.json", "r") as f:
        dados = json.load()

    if "extensoes_permitidas" in dados:
        dados["extensoes_permitidas"] = tuple(dados["extensoes_permitidas"])
    return dados