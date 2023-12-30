import os
import shutil

def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(file_path, template_path=None):
    """Create a file. If a template is provided, copy it."""
    with open(file_path, 'w') as file:
        if template_path:
            with open(template_path, 'r') as template:
                shutil.copyfileobj(template, file)
