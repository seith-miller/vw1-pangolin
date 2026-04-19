# cad/

Parametric CAD scripts for the Pangolin armored vehicle, built with [Build123d](https://github.com/gumyr/build123d).

## Structure

- `cad/` — top-level CAD scripts (chassis, hull, turret, etc.)
- `cad/common/` — shared parametric definitions (wheelbase, hull dimensions, armor thickness, and other reusable parameters)

Generated geometry (STEP, STL) is written to `models/` and is gitignored. PNG renders in `models/renders/` are committed for review.
