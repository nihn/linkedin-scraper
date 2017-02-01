from os.path import dirname, join

from setuptools import find_packages, setup

with open(join(dirname(__file__), 'requirements.txt')) as f:
    requirements = f.readlines()

setup(
    name='linkedin-scraper',
    version='0.0.1',
    author='Mateusz Moneta',
    author_email='mateuszmoneta@gmail.com',
    packages=find_packages(),
    install_requires=requirements,
)
