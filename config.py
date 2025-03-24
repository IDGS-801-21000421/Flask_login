import os
from sqlalchemy import create_engine

import urllib

class Config(object):
    SECRET_KEY = 'clave_super_secreta'
    SESSION_COOKIE_SECURE = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin@localhost/login_flask'
