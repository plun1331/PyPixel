# -*- coding: utf-8 -*-

"""Just a setup file."""

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pypixel-api",
    version="0.1.4",
    description="An asynchronous wrapper for the Hypixel API.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/plun1331/PyPixel",
    author="plun1331",
    packages=["PyPixel"],
    include_package_data=True,
    install_requires=["aiohttp", "nbt"],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8'
    ]
)
