# Import the neccessary libraries

import os
from pathlib import Path

# Define the package name

package_name = "Electrecity_Bill_Prediction_EndToEnd_Projects"

# List the files to be created

list_of_files = [
    Path(".github") /"workflows" / ".gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/component/__init__.py",
    f"src/{package_name}/component/c_01_data_ingestion.py",
    f"src/{package_name}/component/c_02_data_validation.py",
    f"src/{package_name}/component/c_03_data_transformation.py",
    f"src/{package_name}/component/c_4_model_tariner.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/commons.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/config/configuration.py",
    f"src/{package_name}/pipelines/__init__.py",
    f"src/{package_name}/pipelines/p_01_data_ingestion.py",
    f"src/{package_name}/pipelines/p_01_data_ingestion.py",
    f"src/{package_name}/pipelines/p_02_data_validation.py",
    f"src/{package_name}/pipelines/p_03_data_transformation.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/entity/configuration_entity.py",
    f"src/{package_name}/constants/__init__.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/logger.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "setup.py",
    "requirements.txt",
    "research/trials.py",
    "templates/home.html",
    "templates/index.html"
]