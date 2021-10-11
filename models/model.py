"""
@author:azi
@file:model.py
@time:2021/9/26
"""
from datetime import datetime
from utills.core import db


class User(db.Model):
    """
    用户的模型
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    avatar = db.Column(db.String(200))
    password = db.Column(db.String(128))


class UserLoginMethod(db.Model):
    """
    用户登陆验证表，尝试使用微信登陆
    """
    __tablename__ = "user_login_method"
    # 主键
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    # 用户登陆方式，WX微信，P手机
    login_method = db.Column(db.String(36), nullable=False)
    # 用户登陆标识，微信ID或手机号
    identification = db.Column(db.String(36), nullable=False)
    # 用户登陆通行码，密码或token
    access_code = db.Column(db.String(36), nullable=True)

