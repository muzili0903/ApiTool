from django.core import serializers

import logging

from common.http import render_json
from common import error

from .models import SqlDispose

logInf = logging.getLogger('inf')
logErr = logging.getLogger('err')


def dispose_data(request):
    datalist = SqlDispose.objects.all()
    datalist = serializers.serialize("json", datalist)
    print(type(datalist))
    return render_json(data=datalist)


def link_test(request):
    pass
