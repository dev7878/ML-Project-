from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = "-e ."


def get_requirements(path: str) -> List[str]:
    """
    This function returns a list of requirements from a file """

    requirements = []
    with open(path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements


setup(

    name='mlproject',
    version='0.0.1',
    author='Dev Patel',
    author_email='devpatel5578@gmail.com',
    pacakges=find_packages(),
    install_requires=get_requirements('requirements.txt')



)
