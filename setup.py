#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='M6',
    version="1.0",
    description="M6",
    long_description="""
        IRISDB-PY-API
    """,
    zip_safe=False,
    packages=find_packages(exclude=('tests',)),
    url="https://github.com/mobigen/IRISDB-PY-API",
)
