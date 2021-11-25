# _*_ coding=utf-8 _*_
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:  # 基本配置类
    HOST = '127.0.0.1'
    appid = 'wx0b64a2c292ee6be0'
    SECRET_KEY = os.getenv('SECRET_KEY', '5c1374a03986c0c1bc9e14c0ad407e8f')
    ITEMS_PER_PAGE = 10


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:NySQL337618@127.0.0.1/retuo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

class TestingConfig(BaseConfig):
    TESTING = TrueWTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'default': DevelopmentConfig
}
