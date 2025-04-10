'''
The setup. py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return list of requirements
    '''
    list_of_requirements = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from the file
            lines = file.readlines()

            # Process each line
            for line in lines:
                requirement = line.strip()
                # Ignore empty lines and '-e .'
                if requirement and not requirement.startswith('-e'):
                    list_of_requirements.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return list_of_requirements

# print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Dhanush Kumar",
    author_email="dhanushkumar4211@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)