#!/usr/bin/python3
# encoding: utf-8
import re
import sys

project_name = '{{cookiecutter.project_name}}'
module_name = '{{cookiecutter.project_slug}}'

if not re.match(r'^[_a-zA-Z][-_a-zA-Z0-9]+$', project_name):
    print("ERROR: project_name ( %s ) is not a valid. re=r'^[_a-zA-Z][-_a-zA-Z0-9]+$'" % project_name)
    # Exit to cancel project
    sys.exit(1)

if not re.match(r'^[_a-zA-Z][_a-zA-Z0-9]+$', module_name):
    print("ERROR: project_slug ( %s ) is not a valid. re=r'^[_a-zA-Z][_a-zA-Z0-9]+$'" % module_name)
    # Exit to cancel project
    sys.exit(1)
