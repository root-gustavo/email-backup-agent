import json
from pathlib import Path
from typing import List, Dict


DEFAULT_CONFIG_PATH = Path("config.json")


def create_config(
    selected_files: List[Dict],
    folder_name: str,
    config_path: Path = DEFAULT_CONFIG_PATH,
) -> None:

    config_data = {
        "folder_name": folder_name,
        "backups": [
            {
                "pst_path": item["path"],
                "size_bytes": item["size_bytes"],
                "size_human": item["size_human"],
                "status": "pending",
                "last_backup": None,
            }
            for item in selected_files
        ],
    }

    with config_path.open("w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=2, ensure_ascii=False)
