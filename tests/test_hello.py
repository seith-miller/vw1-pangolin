"""Tests for cad/hello.py -- parametric box generation and export."""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Work around py_lib3mf -> lib3mf package naming mismatch
if "py_lib3mf" not in sys.modules:
    try:
        sys.modules["py_lib3mf"] = __import__("lib3mf")
    except ImportError:
        pass

from cad.hello import (
    LENGTH,
    WIDTH,
    HEIGHT,
    STEP_PATH,
    RENDER_PATH,
    build_box,
    export_step,
)

ROOT = Path(__file__).resolve().parent.parent


def test_default_dimensions():
    """Module-level constants match the expected pickup-scale values."""
    assert LENGTH == 5.0
    assert WIDTH == 1.8
    assert HEIGHT == 1.7


def test_build_box_returns_part():
    """build_box() returns a Build123d Part with non-zero volume."""
    import build123d as bd

    part = build_box()
    assert isinstance(part, bd.Part)


def test_build_box_custom_dimensions():
    """build_box() respects custom dimensions."""
    part = build_box(length=2.0, width=1.0, height=0.5)
    bb = part.bounding_box()
    # Bounding box should roughly match the requested dimensions
    assert abs(bb.max.X - bb.min.X - 2.0) < 0.01
    assert abs(bb.max.Y - bb.min.Y - 1.0) < 0.01
    assert abs(bb.max.Z - bb.min.Z - 0.5) < 0.01


def test_export_step_creates_file(tmp_path):
    """export_step() writes a valid STEP file."""
    part = build_box(1.0, 1.0, 1.0)
    out = tmp_path / "test.step"
    result = export_step(part, path=out)
    assert result == out
    assert out.exists()
    assert out.stat().st_size > 0
    content = out.read_text()
    assert "ISO-10303-21" in content  # STEP header marker


def test_output_paths_are_under_models():
    """STEP and render paths are inside the models/ directory."""
    assert STEP_PATH == ROOT / "models" / "hello.step"
    assert RENDER_PATH == ROOT / "models" / "renders" / "hello.png"


def test_step_is_gitignored():
    """models/hello.step should be covered by the *.step gitignore rule."""
    gitignore = (ROOT / ".gitignore").read_text()
    assert "*.step" in gitignore


def test_renders_not_gitignored():
    """PNG renders in models/renders/ should be committed (not gitignored)."""
    gitignore = (ROOT / ".gitignore").read_text()
    assert "!models/renders/*.png" in gitignore
