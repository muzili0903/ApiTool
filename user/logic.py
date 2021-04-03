from user.models import User


def user_is_exist(user):
    try:
        User.objects.get(user=user)
    except User.DoesNotExist:
        return False
    return True


def password_is_identical(password, pwd):
    return password != pwd
