from setuptools import find_packages,setup
from typing import List

def get_requirement(file_path:str)->List[str]:
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        [req.replace("\n","") for req in requirement]
        return requirement
        
setup(
    name="DIAMONDPRICE",
    version="0.0.1",
    author="Fazal Rehman",
    author_email="fazal.rehman05m@gmail.com",
    install_requires=get_requirement('requirement.txt'),
    packages=find_packages()
)