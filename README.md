# Folder-CLI
CLI to create folder structures with default code.
##Python

### Installation guide:
It is required to install python to be able to run the program, along with the click package... just that...
* Python: [V.3.10.7](https://www.python.org/downloads/)
* `pip install click`

## Start a new project
Execute the command `python main.py --help` to have knowledge of all the recognized commands, when you want to create new folders in different projects you must execute the command `python main.py option` and provide the rune of the project where the folders will be created. folders, the next step is to run the command `python main.py flutter` to create the main folders **common**, **core**, **data**, **domain**, **features** , finally run the command `python main.py flutter --help` to have more details of all the available options.

To use options you just have to add `python main.py flutter --features` or `python main.py flutter -f` and follow the CLI instructions to create a folder base with the custom name.

```
# python main.py --help

  Este es un CLI para crear carpetas con código por defecto.

Options:
  --help  Show this message and exit.

Commands:
  coming-soon  Crea carpetas con código por defecto para otros proyectos...
  flutter      Crea carpetas con código por defecto para proyectos Flutter.
  option       Configura la ruta del proyecto.
```

```
# python main.py option
Ruta del proyecto: /home/user/folder-cli/src/test
Ruta del proyecto configurada: /home/user/folder-cli/src/test
```

```
# python main.py flutter --help

  Crea carpetas con código por defecto para proyectos Flutter.

Options:
  -co, --common   Crear carpeta y estructura dentro de "common".
  -c, --core      Crear carpeta y estructura dentro de "core".
  -da, --data     Crear carpeta y estructura dentro de "data".
  -do, --domain   Crear carpeta y estructura dentro de "domain".
  -f, --features  Crear carpeta y estructura dentro de "features".
  --help          Show this message and exit.
```
* [Ejemplo 2: con tests en una carpeta aparte](python/Project-Example-2)
* [Ejemplo 3: con scrapy](https://github.com/ssipyga/contratos_argentina)
* [Ejemplo 4: con django](https://github.com/chadad/propiedades)

