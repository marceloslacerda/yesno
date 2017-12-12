#!/usr/bin/env python

import io

from distutils.core import setup
from os import path
from yesno import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yesno',
    version=__version__,
    description='A module that provides common functions for yes/no CLI queries',
    author='Marcelo Lacerda',
    author_email='marceloslacerda@gmail.com',
    url='https://github.com/marceloslacerda/yesno',
    packages=['yesno'],
    long_description=long_description,
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: CLI :: Utilities',
        'License :: BSD',
        'Programming Language :: Python :: 3.4',
    ],
      keywords='query cli function',
)
