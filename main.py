import os
from src.guardian import iniciar_monitoramento
from watchdog.observers import Observer
import src.guardian as gd
import src.config_manager as cfm
ORIGEM="C:/boiler"
DESTINO="D:/plate"
EXTENSOES=('.psd','.docx','.png')

if __name__ == "__main__":
    config_manager = cfm.ConfigManager()
    dados_config = config_manager.carregar_config()
    gd.GuardianHandler()
    if dados_config['silent'] is False:
        pass
    else:
        pass