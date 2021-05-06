import json

from django.conf import settings
from django.http import HttpResponse


def render_json(data, code=0):
    flag = data.get('msg') or None
    if flag is not None:
        d = eval('{}'.format(data['msg']))
        data['msg'] = d
    result = {
        'code': code,
        'data': data
    }
    if settings.DEBUG:
        print(result)
        json_str = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_str = json.dumps(result, ensure_ascii=False, separators=[',', ':'])
    return HttpResponse(json_str)
