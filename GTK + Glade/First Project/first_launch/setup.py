#!/usr/bin/env python

import os
import sys
import types
from setuptools import setup, find_packages
from first_launch import __version__
from babel.messages import frontend as babel

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Get the long description from the README file
with open("README.rst", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="first_launch",
    version=__version__,
    description="",
    author="SESA536078",
    author_email="",
    maintainer="SESA536078",
    license="OSI Approved :: GNU General Public License v2 (GPLv2)",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Programming Language :: Python :: 3",
    ],
    keywords="",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={"console_scripts": ["first_launch=first_launch.main:main"]},
)
