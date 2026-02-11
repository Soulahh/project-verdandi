logo = '''
\t██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██╗   ██╗███████╗██████╗ ██████╗  █████╗ ███╗   ██╗██████╗ ██╗
\t██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██║   ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗████╗  ██║██╔══██╗██║
\t██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ██║   ██║█████╗  ██████╔╝██║  ██║███████║██╔██╗ ██║██║  ██║██║
\t██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ╚██╗ ██╔╝██╔══╝  ██╔══██╗██║  ██║██╔══██║██║╚██╗██║██║  ██║██║
\t██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║        ╚████╔╝ ███████╗██║  ██║██████╔╝██║  ██║██║ ╚████║██████╔╝██║
\t╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝         ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝
                                                                                                                            
'''

import socket
import os
import subprocess
class CommandLineInterface():
    def __init__(self):
        self.clear_command = 'cls' if os.name == 'nt' else 'clear'
        self.hostname = socket.gethostname()
    
    def limpar_tela(self):
        subprocess.call(self.clear_command, shell=True)
    def display_logo(self):
        print(logo)
    def boas_vindas(self):
        print(f"\tBem-vindo(a) ao Sistema Verdandi, {self.hostname}!")
    def iniciar_menu(self):
        self.limpar_tela()
        self.display_logo()
        self.boas_vindas()
        self.exibir_opcoes()
    def exibir_opcoes(self):
        print(f"""
          1 - Iniciar Monitoramento
          2 - Alterar Pasta de Origem
          3 - Alterar Pasta de Destino
          4 - Alterar Extensões Permitidas
          5 - Alterar Exibição de Interface
          6 - Alterar Delay
          0 - Encerrar Programa\n
        """)