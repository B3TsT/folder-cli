# Archivo: configuracion.py
import json
import os

CONFIG_FILE = '.cli_config.json'

class Configuracion:
    @staticmethod
    def guardar(ruta_proyecto):
        """Guarda la configuración en un archivo JSON."""
        configuracion = {'ruta_proyecto': ruta_proyecto}
        with open(CONFIG_FILE, 'w') as f:
            json.dump(configuracion, f)

    @staticmethod
    def cargar():
        """Carga la configuración desde el archivo JSON."""
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                configuracion = json.load(f)
                return configuracion.get('ruta_proyecto', None)
        return None
