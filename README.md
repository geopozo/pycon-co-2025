`PYTHON_GIL=0 uv run marimo edit`

## python freethreaded
Nota: Si eres usuario de Windows no puedes usar Python con freethreaded de forma automática, debes instalar otras dependencias necesarias. Puedes correr este comando para revisar qué versiones tienes de Python:

```sh
uv python list
```

salida:
```sh
cpython-3.14.0a6+freethreaded-windows-x86_64-none              <download available>
cpython-3.14.0a6-windows-x86_64-none                           <download available>
cpython-3.13.2+freethreaded-windows-x86_64-none                <download available>
cpython-3.13.2+freethreaded-windows-x86_64-none                <download available>
cpython-3.9.21-windows-x86_64-none                             <download available>
cpython-3.8.20-windows-x86_64-none                             <download available>
cpython-3.7.9-windows-x86_64-none                              <download available>
```

Encontrarás las versiones de Python marcadas con freethreaded disponibles para usar.

Para instalar la versión deseada puedes usar el siguiente comando:
```sh
uv python install 3.14
```

Si deseas instalar una versión con freethreaded, debes agregar una 't' al final de la versión:
```sh
uv python install 3.14t
```