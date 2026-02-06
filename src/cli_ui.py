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
    def display_logo(self):
        subprocess.call(self.clear_command, shell=True)
        print(logo)
    def iniciar_menu(self):
        print(f"\tBem-vindo(a) ao Sistema Verdandi, {self.hostname}!")
    def exibir_opcoes(self):
        print(f"""
        1 - Iniciar Monitoramento
        2 - Alterar Configurações
        3 - Encerrar Programa
        """)
    def exibir_configuracoes(self):
        print(f"""
            1 - Alterar Pasta de Origem
            2 - Alterar Pasta de Destino
            3 - Alterar Extensões Permitidas
            4 - Alterar Exibição de Interface
            5 - Alterar Delay
        """)