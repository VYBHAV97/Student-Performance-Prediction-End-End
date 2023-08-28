#Building our application as a package so that anyone one can install this package in future use

from setuptools import find_packages,setup

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str) -> list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        #-e . in a requirements.txt file allows you to develop and test a package 
        #without the need to reinstall it every time you make changes. 
        #Any modifications you make to the package's source code will be immediately 
        #reflected in your environment without requiring a new installation.
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        

setup(
    name='MLProject',
    version='0.0.1',
    author='Krish',
    author_email='vybhav000@gmail.com',
    ## find_packages will look for the file name __init__.py in the current folder and considers that as a package
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)