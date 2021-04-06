import logging
import os

from common.http import render_json
from common import error
from ApiTool.settings import BASE_DIR

from .models import User

from .logic import user_is_exist, password_is_identical

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
    pass


def logout(request):
    pass


def user_del(request):
    pass
