import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium", html_head_file="head.html")


@app.cell
def _():
    import asyncio
    import random
    import time

    import viztracer
    import marimo as mo

    return asyncio, mo, time, viztracer


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Título, Presentarse a los Authores

    Geopozo

    ## David:

    linkedin
    Coautor de github-helper y geopozo 

    ## Andrew

    linkedin
    Coautor de choreographer, kaleido
    Coautor de github-helper y geopozo

    ## Información
    - Repositorio (github)
    - Paquete (pypi)

    - geopozo.github.io/loquesea (RO, proabably cambiamos nombre)
    """
    )
    return


@app.cell
def _(mo, time, viztracer):
    # DEFINICIÓN

    def siesta():
        time.sleep(1)

    def gato():
        siesta()
        siesta()
        print("miau")

    def yo():
        siesta()
        print("buen día")

    # CONTAR

    _inicio = time.perf_counter() # marcar hora

    gato() # mi gato
    yo() # yo

    print(f"Duración: {time.perf_counter() - _inicio}") # calcular duración

    # MIRAR FLAMEGRAPH

    with (
        viztracer.VizTracer(
            output_file=( _path := "results/sync_profile.json"),
            verbose=0
        ),
        mo.capture_stdout()
    ):
        gato()
        yo()

    # usar plotly icicle (con convertador) o https://www.speedscope.app/
    return


@app.cell
async def _(asyncio, mo, time, viztracer):
    # DEFINICIÓN

    async def siesta_async():
        await asyncio.sleep(1)

    async def gato_async():
        await siesta_async()
        await siesta_async()
        print("miau")

    async def yo_async():
        await siesta_async()
        print("buen día")

    # CONTAR

    _inicio = time.perf_counter() # marcar hora

    await gato_async()
    await yo_async()

    print(f"Duración: {time.perf_counter() - _inicio}") # calcular duración

    # MIRAR FLAMEGRAPH

    with (
        viztracer.VizTracer(
            output_file=( _path := "results/async_profile.json"),
            verbose=0
        ),
        mo.capture_stdout()
    ):
        await gato_async()
        await yo_async()

    # usar plotly icicle (con convertador) o https://www.speedscope.app/
    return gato_async, yo_async


@app.cell
async def _(asyncio, gato_async, time, yo_async):
    _inicio = time.perf_counter() # marcar hora

    _t1 = asyncio.create_task(gato_async())
    _t2 = asyncio.create_task(yo_async())

    resultados = await asyncio.gather(_t1, _t2) # que python

    print(f"Duración: {time.perf_counter() - _inicio}") # calcular duración
    return


@app.cell(hide_code=True)
def _(mo):
    mo.hstack(
        [
            mo.md(r"""
    # Sincrona
    ```python
    def siesta():
        time.sleep(1)

    def gato():
        siesta()
        siesta()
        print("miau")

    def yo():
        siesta()
        print("buen día")
    ```
    """),
            mo.md(r"""
    # Asincrona
    ```python
    async def siesta_async():
        await asyncio.sleep(1)

    async def gato_async():
        await siesta_async()
        await siesta_async()
        print("miau")

    async def yo_async():
        await siesta_async()
        print("buen día")
    ```"""),
        ],
        justify="center",
        gap=1
    )

    # acá hagamos comparison de flamegraph real
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # Arregular scripts/

    Hacer threads GIL/no-GIL
    # Errores

    Ya vienen de arriba, también desde funciones inocentes (asyncio.sleep)

    ## Usa Try/Finally

    Puedes usar finally para operaciones criticas

    # Gather

    - Como se usa, que hacemos con errors
    - Cancelación
    - Functiona except *?

    # TaskGroup

    - Como se hace un gather()?
    - Si se sale del contexto, se cancelan los errores?
    - Podemos usar callbacks para sobreescribir comportamiento?
      -  Intenta dos veces
      -  Leventar Error Nuevo
    - Grupos de errores
    - Cancelación automatica (context sin context)  

    Quieres seguir? O quieres parar. Qué hacemos. Y qué hacemos cuando nos
    cancelamos.

    # Tres tipos de "esperables"

    # async with, async for
    """
    )
    return


@app.cell
def _(mo):
    import pycon_co_2025_geopozo.dag as dag

    tree = {"A": {"B": ["D", "E"], "C": []}, "X": ["C", "F"]}

    mo.Html(dag.from_function_tree(tree))
    return


@app.cell
def _(mo):
    mo.md(r"""# GIL""")
    return


if __name__ == "__main__":
    app.run()
