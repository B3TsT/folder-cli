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
@click.option('--soon', '-s', is_flag=True, help='Crear carpeta y estructura dentro de "features".')
def coming_soon(features):
    """Crea carpetas con código por defecto para otros proyectos muy pronto..."""
    click.echo('Proximamente...')

if __name__ == '__main__':
    cli()
    