"""
@author:azi
@file:url.py
@time:2021/9/26
"""
from app.api.view.auth import wx_login
from app.api.view.talk import Reply
from retuo import app


app.add_url_rule('/auth/wx_login/', view_func=wx_login.as_view('wx_login'))
app.add_url_rule('/reply', endpoint='reply', view_func=Reply.as_view('reply'))


