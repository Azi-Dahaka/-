# -*- coding:utf-8 -*-
# 1.导入拓展
from flask import Flask
from flask_restful import Api
import config
from app.api.view.auth import wx_login
from app.api.view.talk import Reply

# 2.创建flask应用实例，__name__用来确定资源所在的路径
app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
api = Api(app)

# 3.定义全局变量
# 4.定义路由和视图函数
# 定义restful api
app.add_url_rule('/auth/wxlogin', view_func=wx_login.as_view('wxlogin'))
app.add_url_rule('/reply', view_func=Reply.as_view('reply'))


# 4.启动程序


if __name__ == '__main__':
    app.run(debug=True)
