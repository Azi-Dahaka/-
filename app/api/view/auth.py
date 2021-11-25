# from config import appid,selseid
# import requests, json, time, random
from flask import jsonify, request
from flask.views import MethodView
from app.utills.weixinAuth import *


class wx_login(MethodView):
    def post(self):
        """
        微信登陆
        :return: {'code':200/201,msg:"返回信息",data:data} /  {'errcode':-1,'errmsg':"返回信息"}
        """
        # 前端获取的临时授权码
        code = request.args.get('code')

        # 参数错误
        if code is None:
            return jsonify({'errcode': -1, 'errmsg': "未提交完整参数"})
        # 获取微信用户授权码
        access_code = get_access_code(code=code)
        if access_code is None:
            return jsonify({'errcode': -2, 'errmsg': "获取微信授权失败"})

        # 获取微信用户信息
        wx_user_info = get_userinfo(access_data=access_code)
        if wx_user_info is None:
            return jsonify({'errcode': -3, 'errmsg': "获取微信授权失败"})

        # 验证微信用户信息本平台是否有，
        data = login_or_register(wx_user_info=wx_user_info)
        if data is None:
            return jsonify({'code': 201, 'msg': "注册失败"})
        return jsonify({'code': 200, 'msg': "成功登录", 'data': data})
