class CLIManager():
    def __init__(self,default_config: dict):
        self.config = default_config
        self.default = default_config
         
    def definir_configuracao(self,chave: str,novo_valor):
        if chave not in self.config:
            return
        self.config[chave] = novo_valor
        
    def retornar_valor(self, chave: str):
        if chave not in self.config:
            return None
        return self.config[chave]

    def restaurar_configuracao(self):
        self.config = self.default