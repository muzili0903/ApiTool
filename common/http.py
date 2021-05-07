import json

from django.conf import settings
from django.http import HttpResponse


def render_json(data=None, msg='请求成功', code=0):
    # print(data)
    # flag = data.get('data') or None
    # if flag is not None:
    #   d = eval('{}'.format(data['msg']))
    #    data['msg'] = d
    data = eval('{}'.format(data))
    result = {
        'code': code,
        'msg': msg,
        'data': data
    }
    if settings.DEBUG:
        json_str = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_str = json.dumps(result, ensure_ascii=False, separators=[',', ':'])
    return HttpResponse(json_str)
