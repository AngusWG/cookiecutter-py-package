#!/usr/bin/python3
# encoding: utf-8
"""A setuptools based setup module for {{ cookiecutter.project_slug }}"""

from codecs import open
from os import path
from setuptools import setup, find_packages

import versioneer

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.md'), encoding='utf-8') as history_file:
    history = history_file.read()

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as requirements_file:
    requirements = requirements_file.read()

with open(path.join(here, 'requirements_dev.txt'), encoding='utf-8') as requirements_dev_file:
    requirements_dev = requirements_dev_file.read()

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

ext_modules = []
setup(
    name='{{ cookiecutter.project_slug }}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme + '\n\n' + history,
    author="{{ cookiecutter.github_username }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}',
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.__main__:run_cil',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    test_suite='tests',
    tests_require=requirements_dev,
    ext_modules=ext_modules,
    keywords = '{{ cookiecutter.project_slug }}',
)
