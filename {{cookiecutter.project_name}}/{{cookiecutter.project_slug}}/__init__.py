# -*- coding: utf-8 -*-
from __future__ import print_function
from ._version import get_versions

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = get_versions()['version']
del get_versions


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
