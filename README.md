
Este cuaderno de [marimo](https://marimo.io/) está activado para usar la versión
nueva de python: free-threaded (hilo-libre).

No es necesario, pero para aprovechar las funciones, debes usar una versión
de python > `3.15t`.

Lastimosamente, está versión no está disponible para Windows.

Puedes verificar las versiones disponibles con:

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

## Linux

`PYTHON_GIL=0 uv run marimo edit`

## Windows

`uv run --python 3.14 marimo edit`

## Mac

Tienes que mirar a `uv list python`.
