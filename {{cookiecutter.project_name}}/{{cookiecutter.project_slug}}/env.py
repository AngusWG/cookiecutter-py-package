#!/usr/bin/python3
# encoding: utf-8
import logging

import redis
import sentry_sdk
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy

from {{cookiecutter.project_slug}}.config import conf

if conf.sentry_dns:  # pragma: no cover
    sentry_sdk.init(dsn=conf.sentry_dns, traces_sample_rate=1.0)


def init_log(log):
    log.setLevel(conf.LOG_LEVEL)
    return log


logger = logging.getLogger("{{cookiecutter.project_slug}}")
init_log(logger)
del init_log

app = Flask(__name__)
app.config.from_object(conf)
sql_db = SQLAlchemy(app)
mongo_db = MongoEngine(app)
redis_db = redis.Redis.from_url(conf.redis_url)
