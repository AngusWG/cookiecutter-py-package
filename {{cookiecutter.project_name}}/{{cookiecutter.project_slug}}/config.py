#!/usr/bin/python3
# encoding: utf-8
import os

import yaml
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    大写字母的配置将读入flask app
    """

    LOG_FORMAT = (
        "[%(asctime)s] [%(uuid)s] [%(threadName)s:%(thread)d] [%(levelname)s]: "
        "%(message)s [%(pathname)s <%(lineno)d>]"
    )
    LOG_LEVEL = "INFO"

    # import os ; print(os.urandom(24))
    SECRET_KEY = b""

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_recycle": 1800}

    SQLALCHEMY_DATABASE_URI = "sqlite:///{{cookiecutter.project_slug}}.db"
    MONGODB_SETTINGS = {
        "DB": "{{cookiecutter.project_slug}}",
        "host": "mongodb://<user>:<password>@127.0.0.1:27017/{{cookiecutter.project_slug}}",
    }

    sentry_dns = None
    redis_url = "redis://127.0.0.1:6379"

    {{cookiecutter.project_slug}}_config_path = "{{cookiecutter.project_slug}}_config.yaml"

    def __init__(self):
        """
        >>> os.environ["{{cookiecutter.project_slug}}_config_path"] = os.path.abspath("{{cookiecutter.project_slug}}_config.yaml")
        >>> Config()
        read config.yaml from...
        """
        print("=== Prepare {{cookiecutter.project_slug}} config start ===")

        # read config from env
        uppercase_vars = [var for var in vars(Config) if not var.startswith("__")]

        for var_name in uppercase_vars:
            env_value = os.environ.get(var_name)
            if env_value is not None:
                print(f"read from ENVIRON: var_name = {env_value}")
                setattr(self, var_name, env_value)

        # read config from config file
        if os.path.exists(self.{{cookiecutter.project_slug}}_config_path):
            with open(self.{{cookiecutter.project_slug}}_config_path, "r", encoding="utf8") as f:
                entries = yaml.safe_load(f)
            self.__dict__.update(entries or {})
            print("read {} values: {}".format(self.{{cookiecutter.project_slug}}_config_path, entries))

        print("=== Prepare {{cookiecutter.project_slug}} config finish===")


conf = Config()
