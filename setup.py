from __future__ import with_statement

import os

NAME = 'logicparser'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from setuptools import find_packages


def read_file(path):
    with open(os.path.join(os.path.dirname(__file__), path)) as fp:
        return fp.read()


setup(
    name=NAME,
    version='1.2.0',
    author='Giuseppe "mastrobirraio" Matranga',
    author_email='matrangagiuseppe99@gmail.com',
    maintainer='Giuseppe "mastrobirraio" Matranga',
    license='MIT',
    description='a free layer to create logics for your arguments',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/mastrobirraio/logicparser',
    packages=find_packages(),
    classifiers=[
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Terminals'
    ],
    keywords='args, arguments, argparser, parser, logic, logicparser',
    python_requires='>=3.6'
)
