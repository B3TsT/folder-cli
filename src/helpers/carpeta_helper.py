# Archivo: carpeta_helper.py
import click
import os
from setting.configuracion import Configuracion

class CarpetaHelper:
    @staticmethod
    def obtener_ruta(numero_carpeta):
        """Obtiene la ruta de la carpeta según el número proporcionado."""
        ruta_configurada = Configuracion.cargar()

        if ruta_configurada:
            carpetas = ['core', 'features', 'data', 'domain', 'common']
            if 0 < numero_carpeta <= len(carpetas):
                return os.path.join(ruta_configurada, carpetas[numero_carpeta - 1])

        raise click.ClickException(f'Número de carpeta no válido: {numero_carpeta}')

    @staticmethod
    def ya_creadas(nombre_proyecto, carpetas):
        """Verifica si todas las carpetas ya han sido creadas."""
        for carpeta in carpetas:
            ruta_carpeta_actual = os.path.join(nombre_proyecto, carpeta)
            if not os.path.exists(ruta_carpeta_actual):
                return False
        return True

    @staticmethod
    def crear(nombre_proyecto, carpetas, nombre_carpeta):
        """Crea las carpetas especificadas en la lista dentro del proyecto."""
        if CarpetaHelper.ya_creadas(nombre_proyecto, carpetas):
            click.echo('Ya todas las carpetas han sido creadas.')
            return

        for carpeta in carpetas:
            if nombre_carpeta ==  '':
                ruta_carpeta_actual = os.path.join(nombre_proyecto, carpeta)
            else:
                ruta_carpeta_actual = os.path.join(f'{nombre_proyecto}/{nombre_carpeta}', carpeta)

            os.makedirs(ruta_carpeta_actual)
            click.echo(f'Creada la carpeta: {ruta_carpeta_actual}')

            # Crear el archivo con el nombre del último nivel de la carpeta y extensión .dart
            nombre_archivo = carpeta + ".dart"
            ruta_archivo = os.path.join(ruta_carpeta_actual, nombre_archivo)
            with open(ruta_archivo, 'w') as f:
                f.write(f'// Contenido del archivo {nombre_archivo}')

    @staticmethod
    def buscar_carpeta(nombre_carpeta):
        """Busca y devuelve la ruta de la carpeta en el directorio actual."""
        ruta_configurada = Configuracion.cargar()
        
        if ruta_configurada:
            ruta = os.path.join(ruta_configurada, nombre_carpeta)
            if os.path.exists(ruta):
                return ruta

        raise click.ClickException(f'No se encontró la carpeta "{features}" en la ruta configurada.')
