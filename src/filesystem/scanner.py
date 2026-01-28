from pathlib import Path
from typing import List
import string
import os


EXCLUDED_DIRS = {
    "Windows",
    "Program Files",
    "Program Files (x86)",
    "$Recycle.Bin",
    "System Volume Information",
}


def get_available_drives() -> List[Path]:
    drives = []
    for letter in string.ascii_uppercase:
        drive = Path(f"{letter}:/")
        if drive.exists():
            drives.append(drive)
    return drives


def is_excluded_dir(path: Path) -> bool:
    return path.name in EXCLUDED_DIRS


def scan_for_pst_files_full() -> List[Path]:
    pst_files: List[Path] = []

    for drive in get_available_drives():
        for root, dirs, files in os.walk(drive, topdown=True):
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

            for file in files:
                if file.lower().endswith(".pst"):
                    pst_files.append(Path(root) / file)

    return pst_files
