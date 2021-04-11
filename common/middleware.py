from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from common import error
from common.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    '''用户登陆验证中间件'''
    WHITE_LIST = [
        '/user/register',
        '/user/login',
    ]

    def process_request(self, request):
        # 如果请求的 URL 在白名单内，直接跳过检查
        for path in self.WHITE_LIST:
            if request.path.startswith(path):
                return

        # 进行登陆检查
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return
            except User.DoesNotExist:
                request.session.flush()
        return render_json(error.LOGIN_ERROR_MSG, code=error.LOGIN_ERROR)



class CorsMiddleware(MiddlewareMixin):
    '''处理客 JS 户端的跨域'''

    def process_request(self, request):
        if request.method == 'OPTIONS' and 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = HttpResponse()
            response['Content-Length'] = '0'
            response['Access-Control-Allow-Headers'] = request.META['HTTP_ACCESS_CONTROL_REQUEST_HEADERS']
            response['Access-Control-Allow-Origin'] = '*'
            return response

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
