"""
@author:azi
@file:url.py
@time:2021/9/26
"""


from retuo import app
from api.view.auth import *

app.add_url_rule('/auth/wx_login', view_func=wx_login.as_view('wx_login'))
