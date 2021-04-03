from common.http import render_json
from common import error

from .models import User

from .logic import user_is_exist, password_is_identical


# Create your views here.
def register(request):
    user = request.POST.get('user')
    if user_is_exist(user):
        return render_json({'msg': '该用户已存在'}, code=error.REGISTER_ERROR)
    password = request.POST.get('password')
    pwd = request.POST.get('pwd')
    if password_is_identical(password, pwd):
        return render_json({'msg': '密码不一致，请重新输入密码'}, code=error.REGISTER_ERROR)
    User.objects.create(user=user, password=password)
    return render_json({'msg': '用户注册成功'})



def login(request):
    pass


def logout(request):
    pass


def user_del(request):
    pass
