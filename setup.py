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
    version="0.1.8a",
    description="An asynchronous wrapper for the Hypixel API.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/plun1331/PyPixel",
    include_package_data=True,
    project_urls={
        "Documentation": "https://pypixel.readthedocs.io/en/latest/",
        "Issue tracker": "https://github.com/plun1331/PyPixel/issues",
      },
    author="plun1331",
    packages=["PyPixel", "PyPixel.utils"],
    install_requires=["aiohttp", "nbt"],
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
