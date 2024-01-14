# Archivo: cli.py
import click
from setting.configuracion import Configuracion
from helpers.carpeta_helper import CarpetaHelper
from command_flutter.create_folder import CreateFolder

@click.group()
def cli():
    """Este es un CLI para crear carpetas con código por defecto."""
    pass

@cli.command(name='option')
@click.option('--ruta', prompt='Ruta del proyecto', type=click.Path(file_okay=False, resolve_path=True))
def config(ruta):
    """Configura la ruta del proyecto."""
    click.echo(ruta)
    Configuracion.guardar(ruta)
    click.echo(f'Ruta del proyecto configurada: {ruta}')

@cli.command(name='flutter')
@click.option('--common', '-co', is_flag=True, help='Crear carpeta y estructura dentro de "common".')
@click.option('--core', '-c', is_flag=True, help='Crear carpeta y estructura dentro de "core".')
@click.option('--data', '-da', is_flag=True, help='Crear carpeta y estructura dentro de "data".')
@click.option('--domain', '-do', is_flag=True, help='Crear carpeta y estructura dentro de "domain".')
@click.option('--features', '-f', is_flag=True, help='Crear carpeta y estructura dentro de "features".')
def command_flutter(common, core, data, domain, features):
    CreateFolder.command_flutter(common=common, core=core, data=data, domain=domain, features=features)     

@cli.command()
@click.option('--features', '-f', is_flag=True, help='Crear carpeta y estructura dentro de "features".')
def flutter_features(features):
    """Crea carpetas con código por defecto para proyectos Flutter en la carpeta "features"."""
    if features:
        try:
            carpeta_features = CarpetaHelper.buscar_carpeta_features()
        except click.ClickException as e:
            click.echo(str(e))
            return
    else:
        carpeta_features = click.prompt('Ingrese la ruta de la carpeta "features"', type=click.Path(file_okay=False, resolve_path=True))

    nombre_carpeta = click.prompt('Nombre de la carpeta en "features"', type=str)
    carpetas_flutter = ['features', nombre_carpeta, 'presentation', 'domain', 'data']
    click.echo(f'Carpeta seleccionada: {nombre_carpeta}')

    CarpetaHelper.crear(nombre_proyecto=carpeta_features, carpetas=carpetas_flutter, nombre_carpeta=nombre_carpeta)
    Configuracion.guardar(carpeta_features)

if __name__ == '__main__':
    cli()
    