""" Setup file for pip install -e support
"""
from setuptools import setup

with open("README.md", "r") as in_file:
    markdown = in_file.read()

with open("requirements.txt", "r") as in_file:
    reqs = [line.strip() for line in in_file.readlines()]

setup(
    name="alpha",
    author="Team Project Group9 BYUI Students",
    author_email="ogunniyiowamamwen@gmail.com",
    url="https://github.com/owamamwen1/CSE210-Team-Alpha",
    license="MIT",
    license_files=["LICENSE.md"],
    description="Tool for checking if all modules, classes, and functions have docstrings",
    version="0.1.0",
    long_description=markdown,
    packages=["project"],
    entry_points={"console_scripts": ["alpha=alpha.__main__:main"]},
    install_requires=reqs,
)
