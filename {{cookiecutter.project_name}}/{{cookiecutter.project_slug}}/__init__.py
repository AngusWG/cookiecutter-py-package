#!/usr/bin/python3
# encoding: utf-8
from __future__ import print_function

from ._version import get_versions

__author__ = '{{ cookiecutter.github_username }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = get_versions()['version']
del get_versions
