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
    parser.add_argument('--silent', action='store_true',help='Ativa modo silencioso')
    parser.add_argument('--delay', type=float)
    parser.add_argument('--origem', nargs='?', type=str, help='Define pasta monitorada')
    parser.add_argument('--destino', nargs='?', type=str, help='Define pasta de backup') 
    parser.add_argument('--extensoes', nargs='+', type=str, help='Lista de extensões permitidas')
    parser.add_argument('--mode',nargs='+', type=str, choices=['interactive','script'],help='Define modo de uso')
    return parser

if __name__ == "__main__":
    argumentos_passados = [arg for arg in sys.argv if arg.startswith('-')]
    config_manager = cfm.ConfigManager()
    parser = definir_parser()
    args = parser.parse_args()
    dados_config = config_manager.carregar_config()
    for argumento, valor in vars(args).items(): 
        if valor is not None:
            dados_config[argumento] = valor
    
    if args.silent is True:
        dados_config['silent'] = True
    dados_config['mode'] = 'script' if len(argumentos_passados) > 0 else 'interactive'
    #gd.GuardianHandler()
    if dados_config['mode'] == 'interactive':
        interface = cliui.CommandLineInterface()
        #
    else:
        #passa tudo sem logging
        pass
    myGuardian = gd.GuardianHandler(pasta_origem=dados_config['origem'],
                                    pasta_destino=dados_config['destino'],
                                    extensoes_permitidas=dados_config['extensoes'],
                                    delay_backup=dados_config['delay'])

    observer = Observer()
    observer.schedule(myGuardian,myGuardian.pasta_origem,recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()