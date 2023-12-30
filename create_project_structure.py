import os
import argparse
from utils import create_directory, create_file

def create_project_structure(project_name):
    base_path = os.path.join(os.getcwd(), project_name)

    # Define directories and files to be created
    dirs = [
        'data/raw', 'data/processed', 'data/external',
        'notebooks', 'src', 'models', 'reports/figures'
    ]
    files = {
        'README.md': None,
        'requirements.txt': None,
        'setup.py': None,
        'src/__init__.py': None,
        'reports/report.md': None
    }

    # Create base project directory
    create_directory(base_path)

    # Create subdirectories
    for dir in dirs:
        create_directory(os.path.join(base_path, dir))

    # Create files
    for file, template in files.items():
        create_file(os.path.join(base_path, file), template)

    # Create notebooks with predefined names
    notebook_names = [
        '01_data_exploration.ipynb', '02_data_cleaning.ipynb',
        '03_feature_engineering.ipynb', '04_model_development.ipynb'
    ]
    for name in notebook_names:
        create_file(os.path.join(base_path, 'notebooks', name))

if __name__ == "__main__":
  # Initialize parser
  parser = argparse.ArgumentParser(description='Create a directory structure for a new data science project.')
  
  # Adding required argument - project name
  parser.add_argument('project_name', type=str, help='Name of the project')

  # Parse the arguments
  args = parser.parse_args()

  # Use the provided project name to create the structure
  create_project_structure(args.project_name)
  print(f"Project '{args.project_name}' structure created.")
