"""Hello-world parametric box -- validates the CAD toolchain end-to-end.

Generates a rectangular box with mid-size pickup dimensions, exports a STEP
file to models/hello.step and renders a PNG to models/renders/hello.png.
"""

from pathlib import Path

import build123d as bd
import pyvista as pv

# ---------------------------------------------------------------------------
# Parametric dimensions (metres) -- roughly a mid-size pickup truck footprint
# ---------------------------------------------------------------------------
LENGTH: float = 5.0   # bumper-to-bumper
WIDTH: float = 1.8    # mirror-to-mirror
HEIGHT: float = 1.7   # ground-to-roof

# ---------------------------------------------------------------------------
# Output paths (relative to repo root)
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
STEP_PATH = ROOT / "models" / "hello.step"
RENDER_PATH = ROOT / "models" / "renders" / "hello.png"


def build_box(length: float = LENGTH, width: float = WIDTH, height: float = HEIGHT) -> bd.Part:
    """Return a Build123d Part representing a simple rectangular box."""
    box = bd.Box(length, width, height)
    return bd.Part() + box


def export_step(part: bd.Part, path: Path = STEP_PATH) -> Path:
    """Export *part* to STEP format at *path*."""
    path.parent.mkdir(parents=True, exist_ok=True)
    bd.export_step(part, str(path))
    return path


def export_stl(part: bd.Part, path: Path | None = None) -> Path:
    """Export *part* to STL format (used as intermediate for rendering)."""
    if path is None:
        path = STEP_PATH.with_suffix(".stl")
    path.parent.mkdir(parents=True, exist_ok=True)
    bd.export_stl(part, str(path))
    return path


def render_png(
    part: bd.Part,
    out_path: Path = RENDER_PATH,
    window_size: tuple[int, int] = (1280, 720),
) -> Path:
    """Tessellate *part* to STL, load in PyVista, and save a PNG render."""
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Export a temporary STL for PyVista to read
    stl_path = out_path.parent / "_tmp_render.stl"
    bd.export_stl(part, str(stl_path))

    try:
        mesh = pv.read(str(stl_path))

        plotter = pv.Plotter(off_screen=True, window_size=window_size)
        plotter.add_mesh(mesh, color="steelblue", show_edges=True)
        plotter.add_light(pv.Light(position=(10, 10, 10), intensity=0.8))
        plotter.set_background("white")
        plotter.camera_position = "iso"
        plotter.screenshot(str(out_path))
        plotter.close()
    finally:
        stl_path.unlink(missing_ok=True)

    return out_path


if __name__ == "__main__":
    print(f"Building box: {LENGTH} x {WIDTH} x {HEIGHT} m")
    part = build_box()
    print(f"Exporting STEP -> {STEP_PATH}")
    export_step(part)
    print(f"Rendering PNG -> {RENDER_PATH}")
    render_png(part)
    print("Done.")
