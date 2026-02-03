import json
import os

class ConfigManager():
    def __init__(self):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        raiz_projeto = os.path.dirname(diretorio_atual)
        self.json_path = os.path.join(raiz_projeto,"config.json")
        self.default = {'origem':'./default/origem','destino':'./default/destino','extensoes_permitidas':['.psd','.jpg','.jpeg','.png'],'delay':2}

    def carregar_config(self):
        try:
            with open(self.json_path, "r") as f:
                dados = json.load(f)
                return dados
        except FileNotFoundError:
            return self.default    
        except json.JSONDecodeError as err:
            print(f"[ERRO] Erro ao decodificar arquivo JSON (Formato inválido)\nCarregando configurações padrão")
            return self.default

    def salvar_config(self, dados: dict):
            with open(self.json_path, "w") as f:
                json.dump(dados, f, indent=4)