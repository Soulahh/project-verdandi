import copy
class CLIManager():
    def __init__(self,default_config: dict):
        self.config = copy.deepcopy(default_config)
        self.default = default_config
         
    def definir_configuracao(self,chave: str,novo_valor):
        if chave in self.config:
            self.config[chave] = novo_valor
        
    def retornar_configuracao(self, chave: str):
        return self.config.get(chave)

    def restaurar_configuracao(self):
        self.config = copy.deepcopy(self.default)

    def restaurar_valor(self, chave: str):
        self.config[chave] = copy.deepcopy(self.default[chave])

    def retornar_dicionario(self):
        return self.config