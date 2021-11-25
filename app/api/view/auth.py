from flask.views import MethodView

import config
from app.utills.weixinAuth import WXBizDataCrypt
from flask import jsonify, Flask, request
from app.models.model import *
import json, requests

class wx_login(MethodView):
    def post(self):
        data = json.loads(request.get_data().decode('utf-8'))  # 将前端Json数据转为字典
        # print(data)
        # data = request.form.get('data').decode('utf-8')
        appID = config.DevelopmentConfig.appid  # 开发者关于微信小程序的appID
        appSecret = config.DevelopmentConfig.SECRET_KEY  # 开发者关于微信小程序的appSecret
        code = data['platCode']  # 前端POST过来的微信临时登录凭证code
        encryptedData = data['platUserInfoMap']['encryptedData']
        iv = data['platUserInfoMap']['iv']
        req_params = {
            'appid': appID,
            'secret': appSecret,
            'js_code': code,
            'grant_type': 'authorization_code'
        }
        wx_login_api = 'https://api.weixin.qq.com/sns/jscode2session'
        response_data = requests.get(wx_login_api, params=req_params, verify=False)  # 向API发起GET请求
        resData = response_data.json()
        # print(resData)
        openid = resData['openid']  # 得到用户关于当前小程序的OpenID
        session_key = resData['session_key']  # 得到用户关于当前小程序的会话密钥session_key

        pc = WXBizDataCrypt(appID, session_key) #对用户信息进行解密
        userinfo = pc.decrypt(encryptedData, iv) #获得用户信息
        # print(userinfo)
        '''
        通过判断数据库中用户是否存在来确定添加或返回自定义登录态（若用户不存在则添加；若用户存在，返回用户信息）
        '''

        if User.query.filter(User.openId == userinfo['openId'])



        return jsonify({"code": 200, "msg": "登录成功", "userinfo": userinfo})

