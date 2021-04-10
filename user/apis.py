import logging
import os

from common.http import render_json
from common import error

from .models import User

from .logic import user_is_exist, password_is_identical, user_and_password_identical

logInf = logging.getLogger('inf')
logErr = logging.getLogger('err')


# Create your views here.
def register(request):
    user = request.POST.get('user')
    if user_is_exist(user):
        logErr.error('该用户: %s 已存在' % user)
        return render_json({'msg': '该用户已存在'}, code=error.REGISTER_ERROR)
    password = request.POST.get('password')
    pwd = request.POST.get('pwd')
    if password_is_identical(password, pwd):
        logErr.error('密码不一致，请重新输入密码')
        return render_json({'msg': '密码不一致，请重新输入密码'}, code=error.REGISTER_ERROR)
    User.objects.create(user=user, password=password)
    logInf.info('用户注册成功')
    return render_json({'msg': '用户注册成功'})


def login(request):
    user = request.POST.get('user')
    password = request.POST.get('password')
    u = user_and_password_identical(user, password)
    if u:
        request.session['uid'] = u.id
        logInf.info('用户登录成功 %s' % u.to_dict())
        return render_json({'msg': '用户登录成功', 'data': u.to_dict()})
    return render_json({'msg': '用户或密码错误'})


def logout(request):
    pass


def user_del(request):
    pass
