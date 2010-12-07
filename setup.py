#! /usr/bin/env python

from distutils.core import setup
from table_setter import __version__

long_description = open('README.markdown').read()

setup(
    name = "python-tablefu",
    version = __version__,
    author = "Chris Amico",
    author_email = "eyeseast@gmail.com",
    description = "A tool for presenting spreadsheets and tables in Python, based on ProPublica's TableSetter",
    long_description = long_description,
    packages = ['table_setter', 'table_setter.template'],
    scripts = ['bin/table-setter'],
    url = "http://github.com/eyeseast/python-tablesetter",
    platforms = ['any'],
    classifiers = ["Development Status :: 1 - Alpha",
                   "Intended Audience :: Developers",
                   "Natural Language :: English",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   ],
)