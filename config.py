# _*_ coding=utf-8 _*_
class BaseConfig(object):
    HOST = '127.0.0.1'


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://mysql:MySql337618:@127.0.0.1:3306/'

