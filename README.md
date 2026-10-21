# Banco de proyectos y artículos LIA

Repositorio público de la organización [LIAUNAL](https://github.com/LIAUNAL). **Tablero en línea: <https://liaunal.github.io/bancoProyectosPapersLIA/>**, con constelación 3D, y [servidor MCP](#servidor-mcp) para redactar artículos y propuestas a partir del trabajo previo del laboratorio.

Banco de ideas, novedades y base de redacción con los artículos en revistas y los proyectos de investigación del grupo GCPDS / LIA (Universidad Nacional de Colombia, sede Manizales), **de 2018 a la fecha**: artículos publicados desde 2018 y proyectos en ejecución desde 2018 (inicio o fin ≥ 2018). El corte se cambia con `MIN_YEAR` en `tools/build_bank.py`; los datos 1996–2017 siguen en `data/raw` y `data/summaries`.

## Contenido

| Ruta | Qué contiene |
|------|--------------|
| `articulos/` | Una ficha `.md` por artículo (122): aplicación, problema, propuesta o novedad, resultados, conclusiones, métodos, idea futura y relacionados |
| `proyectos/` | Una ficha `.md` por proyecto (105: 33 de CvLAC con código Hermes `P###` y 72 tomados directamente de Hermes `H<código>` de las cuentas de Álvarez Meza y Castellanos, con su estado): lo anterior más productos tecnológicos, apropiación social, aliados y código Hermes |
| `docs/` | Sitio estático publicado en GitHub Pages: `index.html` con sistema temático, constelación 3D, clústeres e ideas, buscador y línea de tiempo; `constelacion.html` con el visor SOTA de papersmith-ai; `data/bank.json` |
| `data/bank.json` | Todos los registros con temas, clúster y relaciones |
| `data/taxonomy.md` | Taxonomía de 16 temas (T01–T16; T15 espectro/SDR y T16 agentes de IA se añadieron con los proyectos de Hermes) |
| `data/cluster_names.json` | Nombres de los 12 clústeres (los 16 del corpus completo están en `cluster_names_1996-2026.json`) |
| `data/hermes.json` | Mapeo proyecto → código Hermes, QUIPU y convocatoria (80 proyectos; cuentas de Álvarez Meza y Castellanos) |
| `data/raw/hermes_extra.json`, `data/raw/hermes_details.json` | Proyectos de Hermes incorporados (2025–2026, en evaluación y financiados desde 2018) y el texto de su ficha |
| `data/hermes_sin_cvlac.json` | 204 proyectos de Hermes (ambas cuentas) que no aparecen en CvLAC |
| `pyproject.toml`, `tools/banco_lia_mcp.py`, `tools/bank_db.py` | Paquete `banco-lia` con el servidor MCP y su índice SQLite FTS5 |
| `odd/tasks/banco-lia.md` | Especificación y bitácora del trabajo |

## Fuentes

- CvLAC Andrés Marino Álvarez Meza (`cod_rh=0001330950`) y César Germán Castellanos Domínguez (`cod_rh=0000043222`).
- Google Scholar `user=4aUwQtAAAAAJ` (solo se añadieron artículos de revista ausentes en CvLAC).
- Abstracts: OpenAlex, Crossref y Semantic Scholar (286 de 313 artículos). Las fichas sin abstract están marcadas `fuente_resumen: titulo` y se redactaron de forma conservadora, sin cifras.

## Deduplicación

DOI idéntico o similitud de título ≥ 0,85 entre los dos CvLAC y Scholar, más fusiones manuales: versiones ES/EN del mismo proyecto, preprints con versión publicada (SSRN, preprints.org) y registros de CvLAC que solo repetían el título de otro proyecto.

## Ver el tablero

En línea: **<https://liaunal.github.io/bancoProyectosPapersLIA/>** (la constelación 3D a pantalla completa está en [`constelacion.html`](https://liaunal.github.io/bancoProyectosPapersLIA/constelacion.html)). GitHub Pages publica la carpeta `docs/` de la rama `main`, así que cada push que regenere `docs/` actualiza el sitio en uno o dos minutos.

En local:

```bash
bancoLIA ui              # http://localhost:8000, abre el navegador
bancoLIA ui 9000         # otro puerto
bancoLIA ui --no-open    # sin abrir el navegador
bancoLIA build           # regenera articulos/, proyectos/ y docs/
```

Instalación del comando (una vez): `ln -s "$PWD/bin/bancoLIA" ~/.local/bin/bancoLIA` (cualquier carpeta del `PATH` sirve). Sin el comando: `./tools/serve.sh [puerto]`. El servidor escucha solo en `127.0.0.1`.

### Constelación 3D

`docs/constelacion.html` usa el visor SOTA de papersmith-ai. Cada artículo o proyecto es un sistema solar, y sus planetas son aplicación, problema, novedad, clúster, temas, resultados, conclusiones y productos.

- **Controles:** zoom ±, girar ⟲/⟳, inclinar ▲/▼, rotación automática ▶/⏸, reiniciar vista, «Disposición de grupos» (agrupa por clúster), selector de clúster y buscador por ID o título.
- **Etiquetas:** no hay nombres fijos en el cielo; el nombre de un nodo solo aparece al pasar el cursor.
- **Clic:** ilumina el nodo, su sistema, sus conexiones y sus 5 más relacionados, y abre un panel con la ficha y el top 5 (clic en uno vuela hasta él).
- **Doble clic:** vuela hasta el nodo. `constelacion.html?focus=A060` abre con un sistema seleccionado.

Prueba de calidad visual y funcional (Playwright con el Chrome del sistema, con el tablero levantado):

```bash
uv run --no-project --with playwright --with pillow python tools/qa_constellation.py http://localhost:8000/
```

Verifica en 1440×900, 1280×720, 390×844 y una pantalla de 5760×3088 con el navegador al 50 % de zoom:
- que el grafo se dibuje centrado y que no aparezca el tooltip en reposo;
- la etiqueta del hover dentro del lienzo;
- el panel con el top 5, sin traslapes ni desbordes;
- los controles, el buscador y el filtro;
- la ausencia de errores de JavaScript.

Los nombres de artículos y proyectos aparecen junto a sus soles sin taparse entre sí (acercar muestra más); el botón **nombres** los oculta. Sin una GPU apropiada para WebGL, la pestaña muestra la constelación en 2D con un aviso; `constelacion.html?view=2d` fuerza esa vista.

Mientras otra pestaña del tablero está a la vista, la constelación deja de dibujar. Prueba de memoria y CPU al ir y volver entre pestañas (12 vueltas por defecto):

```bash
uv run --no-project --with playwright python tools/qa_memory.py http://localhost:8000/ [vueltas]
```

Falla si el heap de JS, los nodos del DOM o los listeners siguen creciendo, si la constelación oculta consume más del 5 % de un núcleo o si visible baja de 40 fps.

## Servidor MCP

El servidor MCP (stdio) expone el banco como insumo para escribir artículos (papers_smith) y propuestas (RedaccionPropuestas). Busca sobre un índice SQLite FTS5 (BM25, sin tildes) que se regenera solo cuando cambia `data/bank.json`; el índice no se versiona.

Se instala desde GitHub con [uv](https://docs.astral.sh/uv/), sin clonar el repositorio:

```bash
uvx --from git+https://github.com/LIAUNAL/bancoProyectosPapersLIA banco-lia-mcp
```

El repositorio es privado: hace falta acceso a la organización LIAUNAL y que git pueda autenticarse en GitHub (una vez: `gh auth setup-git`). El paquete trae el servidor, `data/bank.json` y las fichas; el índice queda en `~/.cache/banco-lia/bank.db`. Para tomar una versión nueva del banco: `uvx --refresh --from git+https://github.com/LIAUNAL/bancoProyectosPapersLIA banco-lia-mcp`.

Desde un clon local, `bancoLIA mcp` sirve los datos del clon y guarda el índice en `data/bank.db`.

| Herramienta | Para qué |
|---|---|
| `search_bank` | Búsqueda por texto con filtros `kind`, `cluster`, `topic`, `year_from`; `match` `any` (alguna palabra) o `all` (todas) |
| `get_item` | Registro completo y ficha Markdown de un artículo o proyecto |
| `related_items` | Enlaces proyecto → artículo y artículo → artículo, top 5 similares y mismo clúster |
| `lab_capabilities` | Aliados, financiadores, productos tecnológicos y métodos del laboratorio para un tema, con los ítems que los respaldan |
| `taxonomy` | Temas y clústeres con su número de ítems |
| `export_to_insumos` | Copia fichas Markdown a una carpeta existente, p. ej. `proposals/<run>/insumos/background` |

Registro en un proyecto (`.mcp.json`), como en papersmith-ai y RedaccionPropuestas:

```json
"banco-lia": {
  "type": "stdio",
  "command": "uvx",
  "args": ["--from", "git+https://github.com/LIAUNAL/bancoProyectosPapersLIA", "banco-lia-mcp"]
}
```

La primera ejecución descarga y compila el paquete (unos segundos); las siguientes usan la caché de uv.

Pruebas del índice: `python3 -m unittest discover -s tests`. Consulta rápida desde la terminal: `python3 tools/bank_db.py search "visión por computador"`.

## Regenerar

```bash
uv run --no-project --with scikit-learn --with numpy python tools/build_bank.py
```

Los resúmenes estructurados viven en `data/summaries/*.jsonl`; edítelos ahí y regenere. Para mapear Hermes, llene `data/hermes.json` así:

```json
{"P001": {"codigo": "12345", "aliados": ["Hospital Universitario de Caldas"]}}
```

## Notas de calidad

- `A247` y `A260`: el DOI registrado en CvLAC apunta a otro trabajo o está truncado; se omitió.
- `P032`: CvLAC repite el resumen de `P031`; la ficha se infirió del título.
- Las relaciones «produjo» (proyecto → artículo) y «extiende» (artículo → artículo previo) son similitud semántica, no vínculos declarados. Confírmelas antes de citarlas.

El visor 3D en `vendor/papersmith/` proviene de LIAUNAL/papersmith-ai (Apache-2.0) y empaqueta three.js (MIT). Se conserva idéntico a upstream; la plantilla `tools/constellation_template.html` y los parches `VIEWER_PATCHES` de `tools/build_bank.py` (etiqueta del hover y controles de cámara) se aplican al generar el sitio.
