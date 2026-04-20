# cad/

Parametric CAD scripts for the Pangolin armored vehicle, built with [Build123d](https://github.com/gumyr/build123d).

## Quick start

```bash
# 1. Clone the repo and enter it
git clone <repo-url> && cd vw1-pangolin

# 2. Create a virtualenv and install in editable mode with dev extras
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# 3. Run the hello-world script to verify the toolchain
python cad/hello.py
```

`hello.py` builds a simple parametric box, exports a STEP file, and renders a PNG preview. If it completes without errors the toolchain is working.

## Project structure

| Path | Committed? | Purpose |
|---|---|---|
| `cad/` | yes | Top-level CAD scripts (one per model) |
| `cad/common/` | yes | Shared parametric definitions (wheelbase, armor thickness, etc.) |
| `models/*.step`, `*.stl` | **no** (gitignored) | Generated geometry — rebuild locally |
| `models/*.msh` | **no** (gitignored) | Gmsh mesh files |
| `models/renders/*.png` | **yes** | PNG renders — committed for design review |

See `.gitignore` at the repo root for the full list of ignored patterns.

## Running a CAD script

Each script in `cad/` is runnable standalone:

```bash
python cad/hello.py
```

Outputs:
- `models/hello.step` — STEP geometry (gitignored)
- `models/renders/hello.png` — PNG render (committed)

## Adding a new parametric model

1. Create `cad/<name>.py` with a `build_*()` function that returns a `bd.Part`.
2. Add `export_step()` and `render_png()` calls (see `hello.py` for the pattern).
3. Write outputs to `models/<name>.step` and `models/renders/<name>.png`.
4. Add tests in `tests/test_<name>.py` — at minimum assert the part is a valid solid and the STEP file is created.
5. Run `pytest -v` to verify, then commit the script, tests, and any new PNG renders.

## Toolchain overview

| Library | Role |
|---|---|
| [Build123d](https://github.com/gumyr/build123d) | Parametric solid modelling (BREP). Used to define geometry and export STEP/STL. |
| [Gmsh](https://gmsh.info/) | Mesh generation for FEA. Reads STEP, writes `.msh` files. |
| [PyVista](https://docs.pyvista.org/) | 3-D visualisation and off-screen PNG rendering. |

All three are installed automatically via `pip install -e ".[dev]"` (declared in `pyproject.toml`).

## Running tests

```bash
pytest -v
```

Tests live in `tests/` and cover geometry validity, file export, and project scaffolding checks.
