from src.filesystem.scanner import scan_for_pst_files_full

def main():
    print("Iniciando varredura completa de arquivos PST...")
    pst_files = scan_for_pst_files_full()

    if not pst_files:
        print("Nenhum arquivo PST encontrado.")
        return

    print(f"\nEncontrados {len(pst_files)} arquivos PST:\n")
    for pst in pst_files:
        print(pst)


if __name__ == "__main__":
    main()