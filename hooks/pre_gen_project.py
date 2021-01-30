import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

project_name = '{{cookiecutter.project_name}}'
module_name = '{{cookiecutter.project_slug}}'

if not re.match(MODULE_REGEX, project_name):
    print('ERROR: The project name (%s) is not a valid name. Please do not use a space and use - instead' % module_name)
    #Exit to cancel project
    sys.exit(1)
if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)
    #Exit to cancel project
    sys.exit(1)