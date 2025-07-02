import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


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
def _(time, viztracer):
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
    ):
        gato()
        yo()

    # usar plotly icicle (con convertador) o https://www.speedscope.app/
    return


@app.cell
async def _(asyncio, time, viztracer):
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


@app.cell(hide_code=True)
def _(mo):
    mo.Html("""<svg xmlns="http://www.w3.org/2000/svg" class="release-cycle-chart" viewBox="0 0 828 378.0">
        <defs>
            <linearGradient id="release-cycle-mask-gradient-active">
                <stop stop-color="black" offset="0%"/>
                <stop stop-color="white" offset="100%"/>
            </linearGradient>
        </defs>


                <!-- Row shading -->
                <rect class="release-cycle-row-shade" x="0em" y="6.75" width="828" height="27.0" style="fill:rgb(68, 68, 68); stroke:none; stroke-width:1px; "/>

                <!-- Row shading -->
                <rect class="release-cycle-row-shade" x="0em" y="60.75" width="828" height="27.0" style="fill:rgb(68, 68, 68); stroke:none; stroke-width:1px; "/>


                <!-- Row shading -->
                <rect class="release-cycle-row-shade" x="0em" y="114.75" width="828" height="27.0" style="fill:rgb(68, 68, 68); stroke:none; stroke-width:1px; "/>


                <!-- Row shading -->
                <rect class="release-cycle-row-shade" x="0em" y="168.75" width="828" height="27.0" style="fill:rgb(68, 68, 68); stroke:none; stroke-width:1px; "/>


                <!-- Row shading -->
                <rect class="release-cycle-row-shade" x="0em" y="222.75" width="828" height="27.0" style="fill:rgb(68, 68, 68); stroke:none; stroke-width:1px; "/>


                <!-- Row shading -->
                <rect class="release-cycle-row-shade" x="0em" y="276.75" width="828" height="27.0" style="fill:rgb(68, 68, 68); stroke:none; stroke-width:1px; "/>


            <text class="release-cycle-year-text" x="121.39975247524754" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '19
            </text>
            <line class="release-cycle-year-line" x1="149.85891089108912" x2="149.85891089108912" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="178.39603960396042" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '20
            </text>
            <line class="release-cycle-year-line" x1="206.9331683168317" x2="206.9331683168317" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="235.39232673267327" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '21
            </text>
            <line class="release-cycle-year-line" x1="263.8514851485148" x2="263.8514851485148" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="292.3106435643564" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '22
            </text>
            <line class="release-cycle-year-line" x1="320.769801980198" x2="320.769801980198" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="349.2289603960396" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '23
            </text>
            <line class="release-cycle-year-line" x1="377.68811881188117" x2="377.68811881188117" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="406.2252475247525" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '24
            </text>
            <line class="release-cycle-year-line" x1="434.76237623762376" x2="434.76237623762376" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="463.22153465346537" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '25
            </text>
            <line class="release-cycle-year-line" x1="491.6806930693069" x2="491.6806930693069" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="520.1398514851485" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '26
            </text>
            <line class="release-cycle-year-line" x1="548.5990099009902" x2="548.5990099009902" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="577.0581683168316" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '27
            </text>
            <line class="release-cycle-year-line" x1="605.5173267326732" x2="605.5173267326732" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="634.0544554455445" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '28
            </text>
            <line class="release-cycle-year-line" x1="662.5915841584158" x2="662.5915841584158" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="691.0507425742574" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '29
            </text>
            <line class="release-cycle-year-line" x1="719.5099009900989" x2="719.5099009900989" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="747.9690594059406" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '30
            </text>
            <line class="release-cycle-year-line" x1="776.4282178217823" x2="776.4282178217823" y1="0" y2="351.0" font-size="18" style="stroke:rgb(207, 208, 208); stroke-width:0.8px; "/>
            <text class="release-cycle-year-text" x="804.8873762376238" y="351.0" font-size="13.5" text-anchor="middle" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:middle; ">
                '31
            </text>

        <!-- Gradient mask to fade out end-of-life versions -->
        <mask id="release-cycle-mask-active">
            <rect x="0" y="0" width="126" height="378.0" fill="black"/>
            <rect x="117.0" y="0" width="9.0" height="378.0" fill="url(#release-cycle-mask-gradient-active)"/>
            <rect x="126" y="0" width="828" height="378.0" fill="white"/>
        </mask>

            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- For EOL releases, use a single rounded rectangle -->
                <rect class="release-cycle-blob release-cycle-blob-full&#xA;                       release-cycle-status-end-of-life" x="-391.0990099009901" y="9.0" width="540.9579207920792" height="22.5" rx="4.5" ry="4.5" mask="url(#release-cycle-mask-active)" style="fill:rgb(221, 34, 0); stroke:rgb(255, 136, 136); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-end-of-life" font-size="13.5" y="25.2" x="154.35891089108912" text-anchor="start" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:start; ">
                end-of-life
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="27.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 2.7
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- For EOL releases, use a single rounded rectangle -->
                <rect class="release-cycle-blob release-cycle-blob-full&#xA;                       release-cycle-status-end-of-life" x="-22.29950495049506" y="63.0" width="284.7475247524753" height="22.5" rx="4.5" ry="4.5" mask="url(#release-cycle-mask-active)" style="fill:rgb(221, 34, 0); stroke:rgb(255, 136, 136); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-end-of-life" font-size="13.5" y="79.2" x="266.9480198019802" text-anchor="start" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:start; ">
                end-of-life
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="81.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.6
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- For EOL releases, use a single rounded rectangle -->
                <rect class="release-cycle-blob release-cycle-blob-full&#xA;                       release-cycle-status-end-of-life" x="63.62376237623762" y="90.0" width="284.7475247524753" height="22.5" rx="4.5" ry="4.5" mask="url(#release-cycle-mask-active)" style="fill:rgb(221, 34, 0); stroke:rgb(255, 136, 136); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-end-of-life" font-size="13.5" y="106.2" x="352.8712871287129" text-anchor="start" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:start; ">
                end-of-life
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="108.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.7
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- For EOL releases, use a single rounded rectangle -->
                <rect class="release-cycle-blob release-cycle-blob-full&#xA;                       release-cycle-status-end-of-life" x="137.53960396039605" y="117.0" width="283.8118811881188" height="22.5" rx="4.5" ry="4.5" mask="url(#release-cycle-mask-active)" style="fill:rgb(221, 34, 0); stroke:rgb(255, 136, 136); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-end-of-life" font-size="13.5" y="133.2" x="425.8514851485148" text-anchor="start" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:start; ">
                end-of-life
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="135.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.8
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- Split the blob using path operations
                     (Move-to, Vertical/Horizontal, Arc, Z=close shape;
                      lowercase means relative to the last point.)
                     We start drawing from the top of the straight boundary
                     between the half-blobs.
                 -->
                <path class="release-cycle-blob release-cycle-status-bugfix" d="&#xA;                    M278.509900990099,144.0v22.5H197.71039603960398a4.5,4.5 90 0 1-4.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 14.5 -4.5&#xA;                    Z" style="fill:rgb(0, 221, 34); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <path class="release-cycle-blob release-cycle-status-security" d="&#xA;                    M278.509900990099,144.0v22.5H472.83415841584167a4.5,4.5 90 0 04.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 0-4.5 -4.5&#xA;                    Z" style="fill:rgb(255, 221, 68); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <!-- Add a common border -->
                <rect class="release-cycle-border release-cycle-status-security" x="193.21039603960398" y="144.0" width="284.12376237623766" height="22.5" rx="4.5" ry="4.5" style="fill:rgba(0, 0, 0, 0); stroke:rgb(255, 136, 0); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-security" font-size="13.5" y="160.2" x="377.92202970297035" text-anchor="middle" style="fill:rgb(0, 0, 0); font-size:13.5px; text-anchor:middle;  color: black;">
                security
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="162.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.9
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- Split the blob using path operations
                     (Move-to, Vertical/Horizontal, Arc, Z=close shape;
                      lowercase means relative to the last point.)
                     We start drawing from the top of the straight boundary
                     between the half-blobs.
                 -->
                <path class="release-cycle-blob release-cycle-status-bugfix" d="&#xA;                    M335.27227722772284,171.0v22.5H254.4727722772277a4.5,4.5 90 0 1-4.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 14.5 -4.5&#xA;                    Z" style="fill:rgb(0, 221, 34); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <path class="release-cycle-blob release-cycle-status-security" d="&#xA;                    M335.27227722772284,171.0v22.5H529.7524752475248a4.5,4.5 90 0 04.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 0-4.5 -4.5&#xA;                    Z" style="fill:rgb(255, 221, 68); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <!-- Add a common border -->
                <rect class="release-cycle-border release-cycle-status-security" x="249.9727722772277" y="171.0" width="284.2797029702971" height="22.5" rx="4.5" ry="4.5" style="fill:rgba(0, 0, 0, 0); stroke:rgb(255, 136, 0); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-security" font-size="13.5" y="187.2" x="434.7623762376238" text-anchor="middle" style="fill:rgb(0, 0, 0); font-size:13.5px; text-anchor:middle;  color: black;">
                security
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="189.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.10
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- Split the blob using path operations
                     (Move-to, Vertical/Horizontal, Arc, Z=close shape;
                      lowercase means relative to the last point.)
                     We start drawing from the top of the straight boundary
                     between the half-blobs.
                 -->
                <path class="release-cycle-blob release-cycle-status-bugfix" d="&#xA;                    M395.30940594059405,198.0v22.5H314.509900990099a4.5,4.5 90 0 1-4.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 14.5 -4.5&#xA;                    Z" style="fill:rgb(0, 221, 34); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <path class="release-cycle-blob release-cycle-status-security" d="&#xA;                    M395.30940594059405,198.0v22.5H586.670792079208a4.5,4.5 90 0 04.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 0-4.5 -4.5&#xA;                    Z" style="fill:rgb(255, 221, 68); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <!-- Add a common border -->
                <rect class="release-cycle-border release-cycle-status-security" x="310.009900990099" y="198.0" width="281.160891089109" height="22.5" rx="4.5" ry="4.5" style="fill:rgba(0, 0, 0, 0); stroke:rgb(255, 136, 0); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-security" font-size="13.5" y="214.2" x="493.24009900990103" text-anchor="middle" style="fill:rgb(0, 0, 0); font-size:13.5px; text-anchor:middle;  color: black;">
                security
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="216.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.11
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- Split the blob using path operations
                     (Move-to, Vertical/Horizontal, Arc, Z=close shape;
                      lowercase means relative to the last point.)
                     We start drawing from the top of the straight boundary
                     between the half-blobs.
                 -->
                <path class="release-cycle-blob release-cycle-status-bugfix" d="&#xA;                    M448.7970297029703,225.0v22.5H367.9975247524752a4.5,4.5 90 0 1-4.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 14.5 -4.5&#xA;                    Z" style="fill:rgb(0, 221, 34); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <path class="release-cycle-blob release-cycle-status-security" d="&#xA;                    M448.7970297029703,225.0v22.5H643.7450495049505a4.5,4.5 90 0 04.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 0-4.5 -4.5&#xA;                    Z" style="fill:rgb(255, 221, 68); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <!-- Add a common border -->
                <rect class="release-cycle-border release-cycle-status-security" x="363.4975247524752" y="225.0" width="284.74752475247533" height="22.5" rx="4.5" ry="4.5" style="fill:rgba(0, 0, 0, 0); stroke:rgb(255, 136, 0); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-security" font-size="13.5" y="241.2" x="548.5210396039604" text-anchor="middle" style="fill:rgb(0, 0, 0); font-size:13.5px; text-anchor:middle; color: black;">
                security
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="243.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.12
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- Split the blob using path operations
                     (Move-to, Vertical/Horizontal, Arc, Z=close shape;
                      lowercase means relative to the last point.)
                     We start drawing from the top of the straight boundary
                     between the half-blobs.
                 -->
                <path class="release-cycle-blob release-cycle-status-bugfix" d="&#xA;                    M535.1881188118812,252.0v22.5H425.8514851485148a4.5,4.5 90 0 1-4.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 14.5 -4.5&#xA;                    Z" style="fill:rgb(0, 221, 34); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <path class="release-cycle-blob release-cycle-status-security" d="&#xA;                    M535.1881188118812,252.0v22.5H700.6633663366337a4.5,4.5 90 0 04.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 0-4.5 -4.5&#xA;                    Z" style="fill:rgb(255, 221, 68); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <!-- Add a common border -->
                <rect class="release-cycle-border release-cycle-status-bugfix" x="421.3514851485148" y="252.0" width="283.81188118811883" height="22.5" rx="4.5" ry="4.5" style="fill:rgba(0, 0, 0, 0); stroke:rgb(0, 136, 68); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-bugfix" font-size="13.5" y="268.2" x="478.269801980198" text-anchor="middle" style="fill:rgb(255, 255, 255); font-size:13.5px; text-anchor:middle; color: black;">
                bugfix
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="270.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.13
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- Split the blob using path operations
                     (Move-to, Vertical/Horizontal, Arc, Z=close shape;
                      lowercase means relative to the last point.)
                     We start drawing from the top of the straight boundary
                     between the half-blobs.
                 -->
                <path class="release-cycle-blob release-cycle-status-bugfix" d="&#xA;                    M592.1064356435643,279.0v22.5H482.76980198019805a4.5,4.5 90 0 1-4.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 14.5 -4.5&#xA;                    Z" style="fill:rgb(0, 221, 34); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <path class="release-cycle-blob release-cycle-status-security" d="&#xA;                    M592.1064356435643,279.0v22.5H757.5816831683169a4.5,4.5 90 0 04.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 0-4.5 -4.5&#xA;                    Z" style="fill:rgb(255, 221, 68); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <!-- Add a common border -->
                <rect class="release-cycle-border release-cycle-status-prerelease" x="478.26980198019805" y="279.0" width="283.81188118811883" height="22.5" rx="4.5" ry="4.5" style="fill:rgba(0, 0, 0, 0); stroke:rgb(0, 100, 0); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-prerelease" font-size="13.5" y="295.2" x="473.76980198019805" text-anchor="end" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:end; ">
                prerelease
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="297.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.14
            </text>
            <!-- Colourful blob with a label. -->



            <!-- bugfix/security blobs need to be split between the two phases.
                Draw the rectangle with two path elements instead.
                Thanks Claude.ai for the initial conversion.
            -->

                <!-- Split the blob using path operations
                     (Move-to, Vertical/Horizontal, Arc, Z=close shape;
                      lowercase means relative to the last point.)
                     We start drawing from the top of the straight boundary
                     between the half-blobs.
                 -->
                <path class="release-cycle-blob release-cycle-status-bugfix" d="&#xA;                    M648.0891089108911,306.0v22.5H538.7524752475248a4.5,4.5 90 0 1-4.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 14.5 -4.5&#xA;                    Z" style="fill:rgb(0, 221, 34); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <path class="release-cycle-blob release-cycle-status-security" d="&#xA;                    M648.0891089108911,306.0v22.5H814.5a4.5,4.5 90 0 04.5 -4.5&#xA;                    v-13.5a4.5,4.5 90 0 0-4.5 -4.5&#xA;                    Z" style="fill:rgb(255, 221, 68); stroke:rgba(0, 0, 0, 0); stroke-width:1.6px; "/>
                <!-- Add a common border -->
                <rect class="release-cycle-border release-cycle-status-feature" x="534.2524752475248" y="306.0" width="284.7475247524752" height="22.5" rx="4.5" ry="4.5" style="fill:rgba(0, 0, 0, 0); stroke:rgb(0, 136, 136); stroke-width:1.6px; "/>

            <!-- Add text before/after/inside the blob -->
            <text class="release-cycle-blob-label release-cycle-status-feature" font-size="13.5" y="322.2" x="529.7524752475248" text-anchor="end" style="fill:rgb(207, 208, 208); font-size:13.5px; text-anchor:end; ">
                feature
            </text>

            <!-- Legend on the left -->
            <text class="release-cycle-version-label" x="9.0" y="324.0" font-size="18" style="fill:rgb(207, 208, 208); font-size:18px; text-anchor:start; ">
                Python 3.15
            </text>

        <!-- A line for today -->
        <line class="release-cycle-today-line" x1="462.98762376237624" x2="462.98762376237624" y1="0" y2="351.0" font-size="18" style="stroke:rgb(61, 148, 255); stroke-width:1.6px; "/>
    </svg>""")
    return


if __name__ == "__main__":
    app.run()
