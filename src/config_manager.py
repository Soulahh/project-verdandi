import json

class ConfigManager():
    def __init__(self):
        self.json_path = "../config.json"
    
    def carregar_config(self):
        try:
            with open(self.json_path, "r") as f:
                dados = json.load(f)
                return dados
        except FileNotFoundError as err:
            return {}    

    def salvar_config(self, dados: dict):
            with open(self.json_path, "w") as f:
                json.dump(dados, f, indent=4)