import os
from src.guardian import iniciar_monitoramento

ORIGEM="C:/boiler"
DESTINO="D:/plate"
EXTENSOES=('.psd','.docx','.png')

if __name__ == "__main__":
    iniciar_monitoramento(
        pasta_destino=DESTINO,
        pasta_origem=ORIGEM,
        extensoes=EXTENSOES,
        delay=2.0
    )