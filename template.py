import os
import logging
from pathlib import Path # for handling file paths

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] :  %(message)s : ')

preject_name = "resale_description_writer"

list_of_files = [
    f"src/{preject_name}/__init__.py",
    f"src/{preject_name}/components/__init__.py",
    f"src/{preject_name}/utils/__init__.py",
    f"src/{preject_name}/utils/common.py",
    f"src/{preject_name}/config/__init__.py",
    f"src/{preject_name}/config/configuration.py",
    f"src/{preject_name}/pipeline/__init__.py",
    f"src/{preject_name}/entity/__init__.py",
    f"src/{preject_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    if not file_path.exists():
        file_dir = file_path.parent
        if not file_dir.exists():
            logging.info(f"Creating directory: {file_dir}")
            os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating file: {file_path}")
        with open(file_path, 'w') as f:
            pass  # Create an empty file