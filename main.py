import sys
import os
import time
import shutil
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#TODO: Tratar dados em um config_loader
PASTA_ORIGEM = os.getenv('PASTA_ORIGEM')
PASTA_DESTINO = os.getenv('PASTA_DESTINO')
EXTENSOES_PERMITIDAS = os.getenv('EXTENSOES_PERMITIDAS')
DELAY_BACKUP = os.getenv('DELAY_BACKUP')

class Guardian(FileSystemEventHandler):
    def __init__(self):
        self.timers = {}
    
    def on_modified(self, event):
       if event.is_directory:
           return
       
       if not event.src_path.lower().endswith(EXTENSOES_PERMITIDAS):
           return
       arquivo = event.src_path

       if arquivo in self.timers:
           self.timers[arquivo].cancel()

       timer = threading.Timer(DELAY_BACKUP, self.realizar_backup, args=[arquivo])
       timer.start()
       self.timers[arquivo] = timer

    def realizar_backup(self, caminho_arq_original):
        try:
            if not os.path.exists(caminho_arq_original):
                return

            nome_base, extensao = os.path.splitext(os.path.basename(caminho_arq_original))
            timestamp = time.strftime("%Y-%m_%d_%H-%M-%S")
            novo_nome = f"{nome_base}_{timestamp}.{extensao}"
            caminho_final = os.path.join(PASTA_DESTINO,novo_nome)
            shutil.copy2(caminho_arq_original,caminho_final)

            if caminho_arq_original in self.timers:
                del self.timers[caminho_arq_original]
            print(f"[SUCCESS] Backup salvo: {novo_nome}")

        except Exception as e:
            print(f"[ERRO] Falha ao copiar {caminho_arq_original}: {e}")

if __name__ == '__main__':
    if not os.path.exists(PASTA_DESTINO):
        os.makedirs(PASTA_DESTINO)

    print(f"Guardian online. Vigiando {PASTA_ORIGEM}")

    event_handler = Guardian()
    observer = Observer()
    observer.schedule(event_handler, PASTA_ORIGEM, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

