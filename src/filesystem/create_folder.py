from config.settings import CREATE_FOLDERS

def create_all_folders(folders = CREATE_FOLDERS):
    for folder in folders:
        folder.mkdir(parents=True, exist_ok=True)
