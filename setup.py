from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]                         # Initializing an empty list 
    with open("requirements.txt","r") as file:
        lines = file.readlines()                         # Reads the line one by one
        for line in lines:          
            requirement= line.strip()                    #Removes the \n from the line 
            if requirement and requirement!='-e .':      #If '-e .' is found in line it will not take it and the rest of requirement will get appended 
                requirement_lst.append(requirement)      
    return requirement_lst

setup(
    name="Network Security Project",
    version="0.0.1",
    author="Siddhant Sharma",
    author_email="sidsharma2401@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)