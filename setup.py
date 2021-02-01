# -*- coding: utf-8 -*-

"""Just a setup file."""

import pathlib
from setuptools import setup
import re
from contextlib import suppress

# Load requirements
with open('requirements.txt') as f:
    requirements = f.read().split('\n')

with open('PyPixel/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

if version.endswith(('a', 'b', 'rc')):
    # append version identifier based on commit count
    with suppress(Exception):
        import subprocess

        p = subprocess.Popen(['git', 'rev-list', '--count', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()
        p = subprocess.Popen(['git', 'rev-parse', '--short', 'HEAD'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            version += '+g' + out.decode('utf-8').strip()

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
with open('{0}/README.md'.format(HERE)) as file:
    README = file.read()

# This call to setup() does all the work
setup(
    name="pypixel-api",
    version=version,
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
    install_requires=requirements,
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
