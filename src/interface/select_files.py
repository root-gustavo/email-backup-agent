from pathlib import Path
from InquirerPy import inquirer
from src.filesystem.scanner import format_size


def _extract_base_name_(pst_path: str) -> str:
    return Path(pst_path).stem

def select_pst_files(pst_files: list[Path]) -> tuple[list[dict], str]:
    choices = [
        {
            "name": f"{pst.name} ({format_size(pst.stat().st_size)})",
            "value": pst
        }
        for pst in pst_files
    ]

    selected: list[Path] = inquirer.checkbox(
        message="Selecione os arquivos PST para backup:",
        choices=choices,
        instruction="Use Espaço para selecionar e Enter para confirmar",
    ).execute()

    if not selected:
        raise RuntimeError("Nenhum arquivo PST selecionado")

    selected_files = [
        {
            "path": str(pst),
            "size_bytes": pst.stat().st_size,
            "size_human": format_size(pst.stat().st_size),
        }
        for pst in selected
    ]

    if len(selected_files) == 1:
        folder_name = _extract_base_name_(selected_files[0]["path"])
        return selected_files, folder_name

    name_choices = [
        {
            "name": _extract_base_name_(item["path"]),
            "value": _extract_base_name_(item["path"]),
        }
        for item in selected_files
    ]

    name_choices.append(
        {"name": "Digitar manualmente", "value": "__manual__"}
    )

    folder_choice = inquirer.select(
        message="Escolha o nome da pasta de backup:",
        choices=name_choices,
    ).execute()

    if folder_choice == "__manual__":
        folder_name = inquirer.text(
            message="Digite o nome da pasta:",
            validate=lambda x: bool(x.strip()),
        ).execute()
    else:
        folder_name = folder_choice

    return selected_files, folder_name
