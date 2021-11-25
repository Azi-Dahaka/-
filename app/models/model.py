"""
@author:azi
@file:model.py
@time:2021/9/26
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import retuo

db = SQLAlchemy(retuo.app)


class User(db.Model):
    """
    用户的模型
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    openId = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False)
    avatar = db.Column(db.String(100))
    # phone = db.Column(db.String(11), unique=True)
    # password = db.Column(db.String(30))
    allowCollect = db.Column(db.Boolean)

    def __init__(self, openId, username, avatar):
        self.openId = openId
        self.username = username
        self.avatar = avatar
        self.allowCollect = False

    def __repr__(self):
        return "(%s, %s, %s, %s, %s)" % (self.id, self.openId, self.username, self.avatar, self.allowCollect)



class collectedData(db.Model):
    """
    用户聊天数据的收集
    """
    __tablename__ = 'collectedData'
    contextTop = db.Column(db.String(50), nullable=False)
    contextBottom = db.Column(db.String(50), nullable=False)





if __name__ == '__main__':
    # 创建数据表
    print(db)
    db.create_all()
    print('创建表')

