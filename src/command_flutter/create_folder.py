# Archivo: create_folder.py
import click
import os
from setting.configuracion import Configuracion
from helpers.carpeta_helper import CarpetaHelper

class CreateFolder:

    @staticmethod
    def common():
        click.echo('Ejecutando common de flutter')
        
    @staticmethod
    def core():
        click.echo('Ejecutando core de flutter')  
        
    @staticmethod
    def data():
        nombre_carpeta='data'
        try:
            carpeta_data = CarpetaHelper.buscar_carpeta(nombre_carpeta=nombre_carpeta)
        except click.ClickException as e:
            click.echo(str(e))
            return
        # nombre_carpeta = click.prompt('Nombre de la carpeta en "data"', type=str)
        carpetas_flutter = ['datasources', 'models', 'repositories', 'http']
        click.echo(f'Carpeta seleccionada: {nombre_carpeta}')
        CarpetaHelper.crear(nombre_proyecto=carpeta_data, carpetas=carpetas_flutter, nombre_carpeta='')
        
    @staticmethod
    def domain():
        click.echo('Ejecutando domain de flutter')
        
    @staticmethod
    def features():
        # if features:
        try:
            carpeta_features = CarpetaHelper.buscar_carpeta(nombre_carpeta='features')
        except click.ClickException as e:
            click.echo(str(e))
            return
        # else:
        #     carpeta_features = click.prompt('Ingrese la ruta de la carpeta "features"', type=click.Path(file_okay=False, resolve_path=True))
        nombre_carpeta = click.prompt('Nombre de la carpeta en "features"', type=str)
        # carpetas_flutter = ['features', nombre_carpeta, 'presentation', 'domain', 'data']
        carpetas_flutter = ['presentation', 'domain', 'data']
        click.echo(f'Carpeta seleccionada: {nombre_carpeta}')
        
        CarpetaHelper.crear(nombre_proyecto=carpeta_features, carpetas=carpetas_flutter, nombre_carpeta=nombre_carpeta)
        # Configuracion.guardar(carpeta_features)
        
    @staticmethod
    def default():
        numero_carpeta = click.prompt('1. core\n2. features\n3. data\n4. domain\n5. common\n6. todas las carpetas\nSeleccione la carpeta a crear', type=click.IntRange(1, 6))

        if numero_carpeta == 6:
            carpetas = ['core', 'features', 'data', 'domain', 'common']
        else:
            carpetas = [carpeta for carpeta in ['core', 'features', 'data', 'domain', 'common'][:numero_carpeta]]

        ruta_proyecto = Configuracion.cargar()
        if not ruta_proyecto:
            raise click.ClickException('La ruta del proyecto no está configurada. Utiliza "config" para configurarla.')

        CarpetaHelper.crear(nombre_proyecto=ruta_proyecto, carpetas=carpetas, nombre_carpeta='')

    @staticmethod
    def command_flutter(common, core, data, domain, features):
        """Crea carpetas con código por defecto para proyectos Flutter."""
        if common:
            CreateFolder.common()
        elif core:
            CreateFolder.core()
        elif data:
            CreateFolder.data()
        elif domain:
            CreateFolder.domain()
        elif features:
            CreateFolder.features()   
        else:
            CreateFolder.default() 