import sys
import os
import time
import shutil
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GuardianHandler(FileSystemEventHandler):
    def __init__(self, pasta_destino,extensoes_permitidas,delay_backup):
        self.timers = {}
        self.pasta_destino = pasta_destino
        self.extensoes = extensoes_permitidas
        self.delay = float(delay_backup)
    
    def on_modified(self, event):
       if event.is_directory:
           return
       
       if not event.src_path.lower().endswith(self.extensoes):
           return
       arquivo = event.src_path

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
            novo_nome = f"{nome_base}_{timestamp}.{extensao}"
            caminho_final = os.path.join(self.pasta_destino,novo_nome)
            shutil.copy2(caminho_arq_original,caminho_final)

            if caminho_arq_original in self.timers:
                del self.timers[caminho_arq_original]
            
            #TODO:Transformar prints em logging
            print(f"[SUCCESS] Backup salvo: {novo_nome}")

        except Exception as e:
            print(f"[ERRO] Falha ao copiar {caminho_arq_original}: {e}")

def iniciar_monitoramento(pasta_origem,pasta_destino,extensoes, delay):
    if not os.path.exists(pasta_destino):
        try:
            os.makedirs(pasta_destino)
        except OSError as e:
            print(f"Erro ao criar {pasta_destino}:{e}")
            return

    print(f"Guardian online. Vigiando {pasta_origem}")

    event_handler = GuardianHandler(pasta_destino,extensoes,delay)
    observer = Observer()
    observer.schedule(event_handler, pasta_origem, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

