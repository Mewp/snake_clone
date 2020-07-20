#!/usr/bin/env python3

from os.path import join, dirname
from setuptools import setup

requirements = open(join(dirname(__file__), 'requirements.txt')).readlines()

setup(
    name='snake_clone',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'snake-clone=snake_clone.__main__:run'
        ]
    }
)
