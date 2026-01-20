from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirememnts_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            for line in lines:
                requirememnts=line.strip()
                #Ignore empty lines and -e.
                if requirememnts and requirememnts!='-e .':
                    requirememnts_list.append(requirememnts)
    except FileNotFoundError:
        print("File not found")
    
    return requirememnts_list

print(get_requirements())


setup(
    name="network",
    version="0.0.1",
    author="Pratik Narawade",
    author_email="ptknarawade01@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements()
)