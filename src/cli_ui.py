import os
import subprocess
class CommandLineInterface():
    def __init__(self):
        self.clear_command = 'cls' if os.name == 'nt' else 'clear'
    def display_logo(self):
        subprocess.call(self.clear_command, shell=True)