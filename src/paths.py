"""Centralised filesystem paths for the application.

All resource locations are resolved relative to the project root so the app
can be launched from any working directory.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

UI_DIR = ROOT / "ui"
DATA_DIR = ROOT / "data"
ASSETS_DIR = ROOT / "assets"

# Runtime files (git-ignored, created on first launch).
DB_PATH = str(ROOT / "typing_test.db")
SESSION_FILE = str(ROOT / "session_file.txt")


def ui(name: str) -> str:
    """Absolute path to a Qt Designer ``.ui`` file."""
    return str(UI_DIR / name)


def data(name: str) -> str:
    """Absolute path to a word-list data file."""
    return str(DATA_DIR / name)


def asset(name: str) -> str:
    """Absolute path to a static asset (icon, image, ...)."""
    return str(ASSETS_DIR / name)
