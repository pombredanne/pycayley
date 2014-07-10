#!/usr/bin/env python

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info < (2, 5):
    raise NotImplementedError("Sorry, you need at least Python 2.5 or Python 3.x to use pycayley.")

import pycayley

setup(name='bottle',
      version=pycayley.__version__,
      description='Simple python client for Cayley Graph Database.',
      long_description=pycayley.__doc__,
      author=pycayley.__author__,
      author_email='basaran.caner@gmail.com',
      url='http://github.com/canerbasaran/pycayley/',
      py_modules=['pycayley'],
      scripts=['pycayley.py'],
      install_requires=['requests'],
      license='MIT',
      platforms='any',
      classifiers=['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.5',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   ],
      )
