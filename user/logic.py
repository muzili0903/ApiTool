import logging
from user.models import User

logInf = logging.getLogger('inf')
logErr = logging.getLogger('err')


def user_is_exist(user):
    try:
        User.objects.get(user=user)
    except User.DoesNotExist as e:
        logInf.info('该用户: %s 不存在' % e)
        return False
    logInf.info('该用户: %s 已存在' % user)
    return True


def password_is_identical(password, pwd):
    return password != pwd


def user_and_password_identical(user, password):
    try:
        user = User.objects.get(user=user)
    except User.DoesNotExist as e:
        logInf.info('用户或密码错误 %s ' % e)
        return False
    if password_is_identical(user.password, password):
        logInf.info('用户或密码错误')
        return False
    logInf.info('用户%s登录成功' % user.user)
    return user
