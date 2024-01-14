# Folder-CLI
CLI to create folder structures with default code.

```
📂src
├── 📂common
│   ├── common.dart
│   ├── 📂styles
│   │   └── styles.dart
│   └── 📂widgets
│       └── widgets.dart
├── 📂core
│   ├── 📂bloc
│   │   └── bloc.dart
│   ├── core.dart
│   ├── 📂foundations
│   │   └── foundations.dart
│   ├── 📂router
│   │   └── router.dart
│   ├── 📂services
│   │   └── services.dart
│   └── 📂utils
│       └── utils.dart
├── 📂data
│   ├── data.dart
│   ├── 📂datasources
│   │   └── datasources.dart
│   ├── 📂http
│   │   └── http.dart
│   ├── 📂models
│   │   └── models.dart
│   └── 📂repositories
│       └── repositories.dart
├── 📂domain
│   ├── 📂datasources
│   │   └── datasources.dart
│   ├── domain.dart
│   ├── 📂either
│   │   └── either.dart
│   ├── 📂entities
│   │   └── entities.dart
│   ├── 📂failures
│   │   └── failures.dart
│   ├── 📂models
│   │   └── models.dart
│   ├── 📂repositories
│   │   └── repositories.dart
│   └── 📂usecases
│       └── usecases.dart
├── 📂features
│   ├── features.dart
│   ├── 📂login
│   │   ├── 📂data
│   │   │   └── data.dart
│   │   ├── 📂domain
│   │   │   └── domain.dart
│   │   └── 📂presentation
│   │       └── presentation.dart
│   └── 📂register
│       ├── 📂data
│       │   └── data.dart
│       ├── 📂domain
│       │   └── domain.dart
│       └── 📂presentation
│           └── presentation.dart
└── main.dart
```

## Python

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
