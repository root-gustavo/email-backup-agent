import sys
from pathlib import Path


def get_base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    else:
        return Path(__file__).resolve().parents[1]

BASE_DIR = get_base_dir()
DATA = BASE_DIR / "data"

CREATE_FOLDERS = [DATA]
