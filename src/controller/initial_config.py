from src.filesystem.scanner import scan_for_pst_files_full
from src.interface.select_files import select_pst_files
from src.infrastructure.json.config_manager import create_config
from src.filesystem.create_folder import create_all_folders

def run_initial_config():
    create_all_folders()
    print("Iniciando varredura completa de arquivos PST...")
    pst_files = scan_for_pst_files_full()

    if not pst_files:
        print("Nenhum arquivo PST encontrado.")
        return

    print(f"\nEncontrados {len(pst_files)} arquivos PST:\n")

    selected_files, folder_name = select_pst_files(pst_files)

    create_config(selected_files, folder_name)

    print("Configuração salva com sucesso!")