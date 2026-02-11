import os
import sys
import time
import argparse
import copy
from watchdog.observers import Observer
import src.guardian as gd
import src.config_manager as cfm
import src.cli as cli
import src.cli_ui as cliui


def definir_parser():
    parser = argparse.ArgumentParser(prog = "verdandi", usage='%(prog)s [options]',description='')
    parser.add_argument('--silent', action='store_const',const=True,default=None,help='Ativa modo silencioso')
    parser.add_argument('--delay', type=float)
    parser.add_argument('--origem', nargs='?', type=str, help='Define pasta monitorada')
    parser.add_argument('--destino', nargs='?', type=str, help='Define pasta de backup') 
    parser.add_argument('--extensoes', nargs='+', type=str, help='Lista de extensões permitidas')
    parser.add_argument('--mode', type=str, choices=['interactive','script'],default=None,help='Define modo de uso')
    return parser

def alterar_setup(cli_manager_instance,config: str):
    print(f"Valor atual: ")
    valor_atual = cli_manager_instance.retornar_configuracao(config)
    print(f"{valor_atual}")
    print("(Digite 'cancelar' para retornar)")
    entrada= input("Alterar para >> ")
    if entrada.lower() == 'cancelar':
        return
    
    if isinstance(valor_atual, bool):
        novo_valor = entrada.lower() in ['true','sim','1','s','yes','y']
    elif isinstance(valor_atual,list):
        novo_valor = [v.strip() for v in entrada.split(',')]
    else:
        novo_valor = entrada
    cli_manager_instance.definir_configuracao(config, novo_valor)
def iniciar_programa(guardian_instance):
    observer = Observer()
    observer.schedule(guardian_instance,guardian_instance.pasta_origem,recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        sys.exit(0)

def instanciar_guardian():
    myGuardian = gd.GuardianHandler(pasta_origem=dados_config['origem'],
        pasta_destino=dados_config['destino'],
        extensoes_permitidas=dados_config['extensoes'],
        delay_backup=dados_config['delay'])
    return myGuardian

def atualizar_guardian(guardian_instance, observer = None):
    if observer is not None:
        observer.stop()
        observer.join()
    observer = Observer()
    observer.schedule(guardian_instance, guardian_instance.pasta_origem, recursive=True)
    observer.start()
    return observer


if __name__ == "__main__":
    config_manager = cfm.ConfigManager()
    dados_config = config_manager.carregar_config()
    parser = definir_parser()
    args = parser.parse_args()
    interface = cliui.CommandLineInterface()
    setup = cli.CLIManager(cfm.DEFAULT_CONFIG)
    for argumento, valor in vars(args).items(): 
        if valor is not None:
            dados_config[argumento] = valor
    if dados_config['mode'] == 'interactive':
        continuar_menu = True
        while continuar_menu:
            interface.iniciar_menu()
            try:
                opcao = int(input(">> "))
            except ValueError:
                continue
            match opcao:
                case 1:
                    myGuardian = instanciar_guardian()
                    print("Iniciando monitoramento!")
                    print(f"Pasta Monitorada: {myGuardian.pasta_origem}")                    
                    iniciar_programa(myGuardian)
                case 2:
                    alterar_setup(setup,"origem")
                case 3:
                    alterar_setup(setup,"destino")
                case 4:
                    alterar_setup(setup,"extensoes")
                case 5:
                    alterar_setup(setup,"silent")
                case 6:
                    alterar_setup(setup,"delay")
                case 0:
                    print("Encerrando o programa...")
                    sys.exit(0)
                case _:
                    print("Comando inválido!")

        #
    else:
        myGuardian = instanciar_guardian()
        iniciar_programa(myGuardian)