from setuptools import find_packages, setup

from typing import List

constant = '-e .'

def get_requirements(file_path:str) -> List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if constant in requirements:
            requirements.remove(constant)
    return requirements




setup(
    name = "mlproject",
    version= "0.0.1",
    author= "surya",
    author_email = "mgtron.278@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements("requirements.txt")
)