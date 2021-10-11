# -*- coding:utf-8 -*-
# 1.导入拓展
from flask import Flask, render_template, request, json
from flask_restful import Resource, Api
import config
# 2.创建flask应用实例，__name__用来确定资源所在的路径
app = Flask(__name__)
app.config.from_object(config['development'])
api = Api(app)
# 3.定义全局变量

# 4.定义路由和视图函数
# 定义restful api




# 4.启动程序


if __name__ == '__main__':
    app.run()
