import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def sala_01(Path, mo):
    mo.vstack([
        mo.image(Path("public/QR_CODE.svg"), "QR Pycon 2025 Geopozo package", 200, 200),
        mo.md("## Como instalar:"),
        mo.md("""
    ```
    uv add pycon-co-2025-geopozo
    PYTHON_GIL=0 uv run marimo edit # si linux
    uv run --python 3.14 marimo edit # si windows
    ```"""), 
    ])
    return


@app.cell(hide_code=True)
def import_02():
    import asyncio # herramientas para asyncio
    import math
    import pprint
    import time # sleep, contar segundos, etc
    from pathlib import Path # operaciónes para archivos

    import viztracer # calcular desempeño de funciones
    import marimo as mo # funciones para este cuaderno
    import plotly.graph_objects as go # gráficos

    # nuestras herramientas
    from pycon_co_2025_geopozo import dag, icicle
    return Path, asyncio, dag, go, icicle, math, mo, pprint, time, viztracer


@app.cell
def intro_03(Path, mo):
    # Andrew Pikul

    mo.vstack(
        [
            mo.Html('<center style="font-size: 3em">El asincronismo y la concurrencia de Python en 2025</center>'),
            mo.hstack(
                [
                    mo.vstack(
                        [
                            mo.md("## Andrew Pikul"),
                            mo.image(Path("public/andrew.png"), rounded=True, width="25em"),
                            mo.md("**Author of**: plotly/choreographer, plotly/kaleido, plotly/pozo, plotly/github-helper"),
                            mo.md("[linkedin](https://www.linkedin.com/in/ajpikul/)"),
                            mo.md("[github](https://github.com/ayjayt)"),
                        ], align="center"
                    ),
                    mo.vstack(
                        [
                            mo.md("## David Angarita Ruiz"),
                            mo.image(Path("public/david.png"), rounded=True, width="25em"),
                            mo.md("**Author of**: choreographer, kaleido, pozo, github-helper"),
                            mo.md("[linkedin](https://www.linkedin.com/in/davidangaritaruiz/)"),
                            mo.md("[github](https://github.com/davidangarita1)"),
                        ], align="center"
                    )
                ],
                justify="space-around",
                align="start",
            ),
        ],
        # The geopozo team www.geopozo.ing
    )
    return


@app.cell(hide_code=True)
def version_04(mo):
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
    </svg>

    source: https://devguide.python.org/versions/"""
    )
    return


@app.cell
def cuatro_jinetes_05(Path, mo):
    mo.image(Path("public/cuatro_gatos.svg"))
    return


@app.cell
def gato_sync_06(time):
    # DEFINICIÓN
    def siesta():
        time.sleep(1)

    def gato(p=True):
        siesta()
        siesta()
        if p:
            print("miau")

    def yo(p=True):
        siesta()
        if p:
            print("buen día")
    return gato, yo


@app.cell
def sync_dur_07(gato, time, yo):
    # CONTAR
    _inicio = time.perf_counter() # hora inicio

    gato() # mi gato
    yo() # yo

    print(f"Duración: {time.perf_counter() - _inicio}") # calcular duración
    return


@app.cell
def sync_perf_08(Path, gato, go, icicle, math, viztracer, yo):
    # CALCULAR FLAMEGRAPH

    with (
        viztracer.VizTracer(
            output_file=( _path := "results/sync_profile.json"),
            verbose=0
        ),
    ):
        gato(False)
        yo(False)

    ## MOSTRAR GRÁFICO

    _labels, _parents, _values = icicle.from_threads(
        icicle.sort_and_strip_json(Path(_path))
    )

    _fig = go.Figure(go.Icicle(
            labels=_labels,
            parents=_parents,
            values=[math.log1p(v) for v in _values],
            branchvalues="remainder",
            textinfo="label",
            textfont=dict(size=20),
            marker=dict(
                line=dict(
                width=2,
                color="black"
                ),
            ),
            tiling = dict(
                orientation='v',
            )
        ))
    _fig.update_layout(
            title="Perfíl por Hilo",
            margin=dict(l=10, r=10, t=40, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
    _fig.show() # o https://www.speedscope.app/ # TO lots otros
    return


@app.cell
def gato_async_09(asyncio):
    # DEFINICIÓN

    async def siesta_async(): # estas son corrutinas
        await asyncio.sleep(1)

    async def gato_async(p=True):
        await siesta_async()
        await siesta_async()
        if p:
            print("miau")

    async def yo_async(p=True):
        await siesta_async()
        if p:
            print("buen día")
    return gato_async, yo_async


@app.cell
async def gato_dur_10(gato_async, time, yo_async):
    # CONTAR

    _inicio = time.perf_counter() # hora inicio

    await gato_async()
    await yo_async()

    print(f"Duración: {time.perf_counter() - _inicio}") # calcular duración
    return


@app.cell
async def gato_perf_11(
    Path,
    gato_async,
    go,
    icicle,
    math,
    viztracer,
    yo_async,
):
    # MIRAR FLAMEGRAPH

    with (
        viztracer.VizTracer(
            output_file=( _path := "results/async_profile.json"),
            verbose=0
        ),
    ):
        await gato_async(False)
        await yo_async(False)

    _labels, _parents, _values = icicle.from_threads(
        icicle.sort_and_strip_json(Path(_path))
    )

    _fig = go.Figure(go.Icicle(
            labels=_labels,
            parents=_parents,
            values=[math.log1p(v) for v in _values],
            branchvalues="remainder",
            textinfo="label",
            textfont=dict(size=20),
            marker=dict(
                line=dict(
                width=2,
                color="black"
                ),
            ),
            tiling = dict(
                orientation='v',
            )
        ))
    _fig.update_layout(
            title="Perfíl por Hilo",
            margin=dict(l=10, r=10, t=40, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )
    _fig.show() # o https://www.speedscope.app/
    return


@app.cell
async def gather_gato_12(asyncio, gato_async, time, yo_async):

    _inicio = time.perf_counter() # hora inicio

    resultados = await asyncio.gather(
        gato_async(),
        yo_async()
    )

    print(f"Duración: {time.perf_counter() - _inicio}") # calcular duración
    return


@app.cell(hide_code=True)
def sync_async_13(mo):
    mo.hstack(
        [
            mo.md(r"""
    # Síncrono
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
    # Asíncrono
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

    # acá hacemos comparación del flamegraph real
    return


@app.cell(hide_code=True)
def cheatsheet_14(Path, mo):
    mo.image(Path("public/mug_screenshot.png"))
    return


@app.cell(hide_code=True)
def dag_15(dag, mo):
    tree1 = {dag.Node("gather", "0"): {dag.Node("gato", "1"): ["siesta", "siesta"], "yo": dag.Node("siesta","2")}}
    errors1 = [("1", "0", {})]
    mo.vstack(
        [
            mo.hstack(
                [
                    mo.Html(dag.from_function_tree(tree1, errors1)),
                    mo.md(r"""# Un DAG (Grafo Acíclico Dirigido)
    Ayuda más con el pensamiento.

    ```python
    async def siesta_async():
        await asyncio.sleep(1)

    async def gato_async():
        await siesta_async()
        await siesta_async()
        raise RuntimeError("gato bravo!") # <---
        print("miau")

    async def yo_async():
        await siesta_async()
        print("buen día")

    await asyncio.gather(gato_async(), yo_async())
    ```
            """),
                ],
                justify="start",
                align="center",
                gap=3,
            ),
            mo.md(
    """> ¿Y de dónde vienen los errores? Normalmente desde abajo. Pero con async/await, no. Vienen de todos lados. También, no vemos toda la misma información."""
            ),
        ],
        align="center",
    )
    return (tree1,)


@app.cell(hide_code=True)
def try_16(mo):
    mo.vstack(
        [
            mo.hstack(
                [
                    mo.md(r"""
    ```python
    try:
        await asyncio.gather(
            gato_async(),
            yo_async(),
        )
    except RuntimeError:
        ... # haz algo con los errores
    else:
        ... # si no hay errores! también parte de la familia
    finally:
        ... # haz algo en toda situación
    ```
            """),
                ],
                justify="start",
                align="center",
                gap=3,
            ),
            mo.md(
                """> Pero normalmente tenemos que medir, proporcionar el riesgo de error. Y si es riesgo, hacemos envoltura de try/await. ¿Pero qué peligro hay en un gato dormido?"""
            ),
        ],
        align="center",
    )
    return


@app.cell(hide_code=True)
def timeout_17(dag, mo, tree1):
    tree2 = {dag.Node("timeout", "-1"): tree1}
    errors2 = [
        ("-1", "1", {}),
        ("-1", "2", {}),
    ]

    mo.vstack(
        [
            mo.hstack(
                [
                    mo.Html(dag.from_function_tree(tree2,errors2)),
                    mo.md(r"""
    ```python
    # python v3.11
    async with asyncio.timeout(0.5):
        await una_api.gato_y_yo()
    ```
            """),
                ],
                justify="start",
                align="center",
                gap=3,
            ),
            mo.md(
                """> Si nosotros creamos un API, los usuarios pueden cancelar nuestras tareas sin permiso. ¿Qué hacemos con los errores? ¿Cancelar? ¿Capturarlos para crear uno solo? En este caso, se cancela todo."""
            ),
        ],
        align="center",
    )
    return


@app.function
async def co_mal_impar(i):
    if i in (0, 2, 4, 6, 8, 10):
        return i
    raise ValueError(f"Error: {str(i)} es impar")


@app.cell
async def ret_exc_19(asyncio, pprint):
    _t = [co_mal_impar(i) for i in range(10)]
    _r = await asyncio.gather(*_t, return_exceptions=True)

    # Todo va a seguir hasta el fin, no hay cancelación. Es lo contrario de arriba.

    print("")
    print("Resultado:")
    print("")
    pprint.pp(_r)
    return


@app.cell(hide_code=True)
def rest_tree_20(Path, dag, mo):
    _node = dag.Node("gather", "1")

    tree3 = {"iniciar": [{"REST": _node} for i in range(5)]}
    errors3 = []

    mo.vstack(
        [
            mo.md(
                "[geopozo/github-helper](https://www.github.com/geopozo/github-helper)"
            ),
            mo.Html(dag.from_function_tree(tree3, errors3)),
            mo.image(
                Path("public/gh_helper_screenshot.png"),
            ),
            mo.md(
                """> Código abierto. Mucho llamadas de rest.
                Paralelo por utilizar otros servidores. Microservicios.
                Hemos visto cancelar nada y cancelar todo. 'Y hay más?"""
            ),
        ],
        align="center",
    )
    return


@app.cell
async def a_mano_21(asyncio):
    async def gato_y_yo_gather():
        try:
            _t = [asyncio.create_task(co_mal_impar(i)) for i in range(3)]
            resultados = await asyncio.gather(*_t) # solo con tareas!
        except Exception as e:
            for t in _t:
                t.cancel()
                # También se pudo cancelar el grupo para lograr el mismo efecto.
            # raise e
            print(e)
        else:
            return resultados

    await gato_y_yo_gather()
    return


@app.cell
async def tg_22(asyncio):
    try:
        async with asyncio.TaskGroup() as _tg: # Python 3.11 # es bueno para envolver
            _s = _tg.create_task(asyncio.sleep(1))
            _g = asyncio.create_task(asyncio.sleep(10))
            _tg.create_task(co_mal_impar(1))
            _tg.create_task(co_mal_impar(3))

    finally:
        print(f"Sleep cancelado: {_s.cancelled()}")
        print(f"Sleep global cancelado: {_g.cancelled()}")
    return


@app.cell
async def e_group_23(asyncio):
    try:
        async with asyncio.TaskGroup() as _tg:
            _s = _tg.create_task(asyncio.sleep(1))
            _tg.create_task(co_mal_impar(1))
            _tg.create_task(co_mal_impar(3))
    except* ValueError as e:
        print("Errores esperados dentro del grupo.")
    finally:
        print(f"Sleep cancelado: {_s.cancelled()}")
    return


@app.cell
def thread_24():
    # con no-GIL
    import sys; print(sys._is_gil_enabled()) # PEP 703
    # no todo funciona (no hagas conversiones)


    from threading import Thread

    # shared state
    counter = 0

    def hilo():
        global counter
        for _ in range(10_000_000):
            counter += 1

    if __name__ == "__main__":
        _t1 = Thread(target = hilo)
        _t2 = Thread(target = hilo)
        _t1.start()
        _t2.start()
        _t1.join()
        _t2.join()

        print(counter)  # → Final counter value: 2000
    return (Thread,)


@app.cell
def thread_25(Thread):
    # con no-GIL, tienes que hacer todo a mano.
    from threading import Lock

    # shared state
    counter_locked = 0
    lock = Lock()

    def hilo_locked():
        global counter_locked
        for _ in range(10_000_000):
            with lock:
                counter_locked += 1


    _t1 = Thread(target = hilo_locked)
    _t2 = Thread(target = hilo_locked)
    _t1.start()
    _t2.start()
    _t1.join()
    _t2.join()

    print(counter_locked)  # → Final counter value: 2000
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
