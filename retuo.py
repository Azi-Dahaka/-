# -*- coding:utf-8 -*-
# 1.导入拓展
from flask import Flask, render_template, request, json
from flask_restful import Resource, Api
# 2.创建flask应用实例，__name__用来确定资源所在的路径
app = Flask(__name__)
api = Api(app)
# 3.定义全局变量
todos= {}
# 4.定义路由和视图函数
# 定义restful api


class HelloWorld(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


api.add_resource(HelloWorld, '/test/<string:todo_id>')

# 4.启动程序


if __name__ == '__main__':
    app.run()
