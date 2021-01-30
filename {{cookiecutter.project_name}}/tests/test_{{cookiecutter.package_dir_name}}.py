#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_{{ cookiecutter.package_dir_name }}
----------------------------------

Tests for `{{ cookiecutter.package_dir_name }}` module.
"""
import pytest
import {{ cookiecutter.project_slug }}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')



class Test{{ cookiecutter.project_slug|capitalize }}:

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_something(self):
        assert {{ cookiecutter.project_slug}}.__version__
