from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Returns list of requirements
    """
    requirements = []
    with open(file_path) as f: 
        requirements = f.readlines() 
        requirements = [req.replace('\n','') for req in requirements[:-1]]
        # if '-e .' in requirements:
        #     requirements.remove('-e .')
    return requirements


setup(
name = 'mlproject',
version = '0.0.1',
author = 'Manideep',
author_email = 's@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt') 
)