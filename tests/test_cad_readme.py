"""Tests for cad/README.md content completeness."""

from pathlib import Path

README = (Path(__file__).resolve().parent.parent / "cad" / "README.md").read_text()


def test_installation_instructions():
    """README explains how to install the toolchain."""
    assert "pip install -e" in README


def test_hello_py_example():
    """README shows how to run the hello-world script."""
    assert "hello.py" in README
    assert "python cad/hello.py" in README


def test_outputs_documented():
    """README documents where STEP and PNG outputs land."""
    assert "models/" in README
    assert "models/renders/" in README


def test_gitignored_vs_committed():
    """README distinguishes gitignored from committed files."""
    assert "gitignored" in README.lower() or "gitignore" in README.lower()
    assert ".step" in README or "STEP" in README
    assert ".png" in README or "PNG" in README


def test_new_model_instructions():
    """README explains how to add a new parametric model."""
    assert "adding a new" in README.lower() or "add a new" in README.lower()


def test_toolchain_overview():
    """README mentions Build123d, Gmsh, and PyVista."""
    assert "Build123d" in README
    assert "Gmsh" in README
    assert "PyVista" in README
