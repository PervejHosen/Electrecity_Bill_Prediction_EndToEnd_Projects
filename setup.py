from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT_REQUIREMENT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPHEN_E_DOT_REQUIREMENT in requirements:
        requirements.remove(HYPHEN_E_DOT_REQUIREMENT)
    
    return requirements


__version__ = "0.0.1"
SRC_REPO = "Electricity_Bill_Prediction_EndToEnd_Projects"

setup(
    name=SRC_REPO,
    version=__version__,
    description="This is a Project to predict the Electricity bills",
    author="Pervej",
    author_email="pervejhosen2@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
