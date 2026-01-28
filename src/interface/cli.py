from pathlib import Path
from InquirerPy import inquirer
from src.filesystem.scanner import format_size


def select_pst_files(pst_files: list[Path]) -> list[str]:
    choices = [
        {
            "name": f"{pst.name} ({format_size(pst.stat().st_size)})",
            "value": str(pst)
        }
        for pst in pst_files
    ]

    selected = inquirer.checkbox(
        message="Selecione os arquivos para backup:",
        choices=choices,
        instruction="Use Espaço para selecionar e Enter para confirmar",
    ).execute()

    return selected
