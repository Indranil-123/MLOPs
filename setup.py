from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(

    name = "project32",
    version = "0.1",
    author = "indranil Bakshi",
    email = "iamneel67@gmail.com",
    packages = find_packages(),
    install_requires = requirements,
    python_requires = ">=3.7"

)
