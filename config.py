# _*_ coding=utf-8 _*_
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:  # 基本配置类
    HOST = '127.0.0.1'
    appid = 'wx0b64a2c292ee6be0'
    SECRET_KEY = os.getenv('SECRET_KEY', 'dddd_retuo')
    ITEMS_PER_PAGE = 10


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:NySQL337618@127.0.0.1/retuo'


class TestingConfig(BaseConfig):
    TESTING = TrueWTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'test': TestingConfig,
    'default': DevelopmentConfig
}
