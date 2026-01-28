from src.filesystem.scanner import scan_for_pst_files_full, format_size
from src.interface.cli import select_pst_files


def main():
    print("Iniciando varredura completa de arquivos PST...")
    pst_files = scan_for_pst_files_full()

    if not pst_files:
        print("Nenhum arquivo PST encontrado.")
        return

    print(f"\nEncontrados {len(pst_files)} arquivos PST:\n")
    for pst in pst_files:
        size = pst.stat().st_size
        print(f"{pst}")
        print(f"  Size: {format_size(size)}\n")

    selected_files = select_pst_files(pst_files)

    print("\nArquivos selecionados:")
    for file in selected_files:
        print(file)


if __name__ == "__main__":
    main()
