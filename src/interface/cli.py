from InquirerPy import inquirer

def select_pst_files(pst_files: list[str]) -> list[str]:
    selected = inquirer.checkbox(
        message="Selecione os arquivos PST para backup:",
        choices=pst_files,
        instruction="Use espaço para selecionar e Enter para confirmar",
    ).execute()

    return selected
