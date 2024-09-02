import os
import sys
import logging
from pathlib import Path

logging.basicConfig(
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

project_name = "MLOPS_Pipeline"

##Helpful in CI/CD pipelines and uplaods non empty folders only
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/compnents/__init__.py",
    f"src/{project_name}/compnents/data_ingestion.py",
    f"src/{project_name}/compnents/data_transformation.py",
    f"src/{project_name}/compnents/model_trainer.py",
    f"src/{project_name}/compnents/model_evaluation.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/utils.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/entitiy/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh"
    "config/gonfig.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "Makefile",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "project.toml",
    "tox.ini",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating Directory: {file_dir} for the file name: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating Empty File: {file_path}")
    else:
        logging.info(f"{file_name} already exists")


    