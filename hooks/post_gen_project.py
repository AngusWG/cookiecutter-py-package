#!/usr/bin/python3
# encoding: utf-8
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if 'n' == '{{ cookiecutter.need_utils_code }}':
        package_dir = "{{cookiecutter.project_slug}}"
        remove_file(os.path.join(package_dir, "config.py"))
        remove_file(os.path.join(package_dir, "env.py"))
        remove_file(os.path.join(package_dir + "_config.yaml"))
