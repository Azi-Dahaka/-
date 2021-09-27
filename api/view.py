from models.model import *
# from config import appid,selseid
import requests, json, time, random
from flask import jsonify, request
from flask.views import MethodView
from  datetime import datetime


class Authentication(MethodView):
    def wx_login:
        """
        微信登陆
        :return: {'code':-1/200/201,msg:"返回信息"}
        """
        # 前端获取的临时授权码
        code= request.args.get('code')
        # 表示登陆方式
        flag = request.args.get("flag")

        #参数错误
        if code is None or flag is None:
            return jsonify({'code':-1,'msg':"未提交完整参数"})

