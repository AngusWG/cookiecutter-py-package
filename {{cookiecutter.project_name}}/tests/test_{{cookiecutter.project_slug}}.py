#!/usr/bin/python3
# encoding: utf-8

"""
test_{{ cookiecutter.project_slug }}
----------------------------------

Tests for `{{ cookiecutter.project_slug }}` module.
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

    def test_something(self, benchmark):
        assert {{ cookiecutter.project_slug}}.__version__
        from {{cookiecutter.project_slug}} import __main__
        # asset cost time
        benchmark(__main__.version())
        assert benchmark.state.state.max < 0.01


{%- if cookiecutter.need_utils_code == "y" %}
    def test_config(self):
        import os
        from {{ cookiecutter.project_slug }}.config import Config, conf
        from {{ cookiecutter.project_slug }}.env import app
        # read flask config
        assert app.config['SQLALCHEMY_DATABASE_URI'] == conf.SQLALCHEMY_DATABASE_URI
        # read config.yaml
        file_name = "config.yaml"
        created_config = False
        if not os.path.exists(file_name):
            created_config = True
            open(file_name, "w", encoding='utf8').write("A: a")
        assert Config().LOG_LEVEL == conf.LOG_LEVEL
        if created_config:
            os.remove(file_name)
{%- endif %}
