# Archivo: create_folder.py
import click
import os
from setting.configuracion import Configuracion
from helpers.carpeta_helper import CarpetaHelper

class CreateFolder:

    @staticmethod
    def common():
        nombre_carpeta='common'
        try:
            carpeta_data = CarpetaHelper.buscar_carpeta(nombre_carpeta=nombre_carpeta)
        except click.ClickException as e:
            click.echo(str(e))
            return
        carpetas_flutter = ['widgets', 'styles']
        click.echo(f'Carpeta seleccionada: {nombre_carpeta}')
        CarpetaHelper.crear(nombre_proyecto=carpeta_data, carpetas=carpetas_flutter, nombre_carpeta='')
        
    @staticmethod
    def core():
        nombre_carpeta='core'
        try:
            carpeta_data = CarpetaHelper.buscar_carpeta(nombre_carpeta=nombre_carpeta)
        except click.ClickException as e:
            click.echo(str(e))
            return
        carpetas_flutter = ['services', 'utils', 'router', 'foundations', 'bloc']
        click.echo(f'Carpeta seleccionada: {nombre_carpeta}')
        CarpetaHelper.crear(nombre_proyecto=carpeta_data, carpetas=carpetas_flutter, nombre_carpeta='') 
        
    @staticmethod
    def data():
        nombre_carpeta='data'
        try:
            carpeta_data = CarpetaHelper.buscar_carpeta(nombre_carpeta=nombre_carpeta)
        except click.ClickException as e:
            click.echo(str(e))
            return
        # nombre_carpeta = click.prompt('Nombre de la carpeta en "data"', type=str)
        carpetas_flutter = ['datasources', 'repositories', 'http']
        click.echo(f'Carpeta seleccionada: {nombre_carpeta}')
        CarpetaHelper.crear(nombre_proyecto=carpeta_data, carpetas=carpetas_flutter, nombre_carpeta='')
        
    @staticmethod
    def domain():
        nombre_carpeta='domain'
        try:
            carpeta_data = CarpetaHelper.buscar_carpeta(nombre_carpeta=nombre_carpeta)
        except click.ClickException as e:
            click.echo(str(e))
            return
        carpetas_flutter = ['entities', 'repositories', 'datasources', 'usecases', 'models', 'either', 'failures']
        click.echo(f'Carpeta seleccionada: {nombre_carpeta}')
        CarpetaHelper.crear(nombre_proyecto=carpeta_data, carpetas=carpetas_flutter, nombre_carpeta='')
        
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
            # carpetas = [carpeta for carpeta in ['core', 'features', 'data', 'domain', 'common'][:numero_carpeta]]
            carpetas = [['core', 'features', 'data', 'domain', 'common'][numero_carpeta-1]]

        ruta_proyecto = Configuracion.cargar()
        if not ruta_proyecto:
            raise click.ClickException('La ruta del proyecto no está configurada. Utiliza "config" para configurarla.')
        
        # print(ruta_proyecto,carpetas, numero_carpeta)
        CarpetaHelper.crear(nombre_proyecto=ruta_proyecto, carpetas=carpetas, nombre_carpeta='')

    @staticmethod
    def command_flutter(common, core, data, domain, features):
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
