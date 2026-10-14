# Montana Angling Pressure, 2019–2020

Montana saw roughly a **28% increase in statewide angling pressure** at the onset of
the 2020 pandemic. This project asks where that increase actually landed.

**Hypothesis:** angling pressure became more *dispersed* during 2020, increasing
proportionally more on less-popular rivers than on the already-busy ones.

Data comes from Montana Fish, Wildlife & Parks angling surveys, which run on the
fishing licence year (March–February), compared across licence years 2019 and 2020,
with base layers from the Montana State Library.

CSCI 502 — Geospatial Data Science, University of Montana.

## Layout

```
Project1_JR.qgz    QGIS project — the cartography
Data/              source and derived geodata (not in this repo, see below)
Notebook/          analysis notebooks and the LaTeX report build
Figures/           map exports and charts
Reports/           submitted PDF and the launch document
Docs/              documentation, survey summaries
```

## The QGIS project

`Project1_JR.qgz` loads ten layers by **relative** path (`./Data/...`), so the `.qgz`
file and the `Data/` folder must stay siblings or the project opens with broken
layers:

| Layer | Source |
|---|---|
| `rivers_2019_final`, `rivers_2020`, `rivers_pctchange_final` | per-river pressure and change |
| `montana_streams_anglingpressure_lakes_removed` | streams with lakes dissolved out |
| `fishing_access_nearRivers2`, `fishing_access_sites__points` | FWP fishing access sites |
| `montana_lakes_INTERSECT_with_streams_DISSOLVED` | lake/stream intersection |
| `montana_cities_POINT`, `MontanaStateBoundary_shp` | reference layers |

## Notebooks

`Notebook/` holds the analysis and the report build. The notebooks reference
`../Data/` and `../Figures/`, so they run from inside that folder.

The report is built notebook → LaTeX → PDF; `fix_title.py` and
`rebuild_pdf_zero_margins.txt` document that step. The `.tex` files contain absolute
container paths (`/home/jovyan/work/Project1/Figures/...`), which is why this folder
must keep the name `Project1` and sit at the root of the mounted course directory.

## Running it

The analysis runs in the `gds-qgis` Docker image from the course root:

```
docker build -t gds-qgis ./docker/gds-qgis
docker run --rm -ti -p 8888:8888 -v "<course-root>:/home/jovyan/work" gds-qgis
```

## Data

`Data/` is **excluded from this repo** — 972 MB of source and derived geodata, past
what belongs in git. It holds FWP angling survey tables, fishing access points,
Montana hydrography and boundaries, and the derived geopackages the QGIS project
reads. The survey summary PDFs for 2019 and 2020 are in `Docs/`.
