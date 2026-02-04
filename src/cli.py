class CLIManager():
    def __init__(self):
        self.dados = {'origem':'./default/origem',
                      'destino':'./default/destino',
                      'extensoes_permitidas':['.psd','.jpg','.jpeg','.png'],
                      'delay':2,
                      'silent':False}
    
    def alterar_dado(self,dado: str,novo_valor):
        if dado not in self.dados:
            return
        self.dados[dado] = novo_valor
        
