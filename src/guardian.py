import sys
import os
import time
import shutil
import threading
from watchdog.events import FileSystemEventHandler

class GuardianHandler(FileSystemEventHandler):
    def __init__(self, pasta_origem, pasta_destino,extensoes_permitidas,delay_backup):
        self.timers = {}
        self.pasta_origem = os.path.abspath(pasta_origem)
        self.pasta_destino = os.path.abspath(pasta_destino) 
        self.extensoes = tuple(extensoes_permitidas)
        self.delay = float(delay_backup)
    
    def on_modified(self, event):
        if event.is_directory:
            return
       
        if not event.src_path.lower().endswith(self.extensoes):
            return
        arquivo = event.src_path

        #Checa se o destino do backup bate com a origem, evitando loop infinito
        common_destiny = os.path.commonpath([os.path.dirname(arquivo), self.pasta_destino])
        if common_destiny == arquivo or common_destiny == self.pasta_destino:
            return
       

        if arquivo in self.timers:
           self.timers[arquivo].cancel()

        timer = threading.Timer(self.delay, self.realizar_backup, args=[arquivo])
        timer.start()
        self.timers[arquivo] = timer

    def realizar_backup(self, caminho_arq_original):
        try:
            if not os.path.exists(caminho_arq_original):
                return

            nome_base, extensao = os.path.splitext(os.path.basename(caminho_arq_original))
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            novo_nome = f"{nome_base}_{timestamp}{extensao}"
            caminho_final = os.path.join(self.pasta_destino,novo_nome)
            shutil.copy2(caminho_arq_original,caminho_final)

            if caminho_arq_original in self.timers:
                self.timers.pop(caminho_arq_original, None)
            
            #TODO:Transformar prints em logging
            print(f"[SUCCESS] Backup salvo: {novo_nome}")

        except Exception as e:
            print(f"[ERRO] Falha ao copiar {caminho_arq_original}: {e}")

