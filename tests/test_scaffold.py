"""Tests that verify the CAD toolchain scaffold is set up correctly."""

import configparser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_directory_structure_exists():
    """Required directories exist."""
    for d in ["cad", "cad/common", "analysis", "models", "models/renders"]:
        assert (ROOT / d).is_dir(), f"Missing directory: {d}"


def test_cad_readme_exists():
    """cad/ has a README stub."""
    readme = ROOT / "cad" / "README.md"
    assert readme.is_file()
    content = readme.read_text()
    assert "Build123d" in content or "build123d" in content.lower()


def test_pyproject_toml_exists_and_has_dependencies():
    """pyproject.toml lists the required dependencies."""
    toml_path = ROOT / "pyproject.toml"
    assert toml_path.is_file()
    content = toml_path.read_text()
    for dep in ["build123d", "gmsh", "pyvista", "numpy"]:
        assert dep in content, f"Missing dependency: {dep}"


def test_pyproject_toml_has_dev_dependencies():
    """pyproject.toml has dev extras with pytest and ruff."""
    content = (ROOT / "pyproject.toml").read_text()
    assert "pytest" in content
    assert "ruff" in content


def test_gitignore_blocks_generated_files():
    """Generated CAD/FEA files are gitignored."""
    gitignore = (ROOT / ".gitignore").read_text()
    for pattern in ["*.step", "*.stl", "*.msh", "*.vtk"]:
        assert pattern in gitignore, f"Missing gitignore pattern: {pattern}"


def test_gitignore_allows_png_renders():
    """PNG renders in models/renders/ are not gitignored."""
    gitignore = (ROOT / ".gitignore").read_text()
    assert "!models/renders/*.png" in gitignore


def test_cad_packages_importable():
    """The cad package (local) is importable."""
    import cad
    import cad.common
