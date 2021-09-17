# -*- coding:utf-8 -*-
# 1.导入拓展
from flask import Flask, render_template, request, json

# 2.创建flask应用实例，__name__用来确定资源所在的路径
app = Flask(__name__)
# 3.定义路由和视图函数
# 装饰器


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# 4.启动程序


if __name__ == '__main__':
    app.run(debug=True)
