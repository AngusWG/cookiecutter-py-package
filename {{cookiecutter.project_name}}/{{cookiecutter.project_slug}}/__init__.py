#!/usr/bin/python3
# encoding: utf-8
from __future__ import print_function

from . import _version

__version__ = _version.get_versions()["version"]

__author__ = "{{ cookiecutter.github_username }}"
__email__ = "{{ cookiecutter.email }}"
