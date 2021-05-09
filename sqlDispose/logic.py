from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage

import logging

from .models import SqlDispose

logInf = logging.getLogger('inf')
logErr = logging.getLogger('err')


# Create your views here.
def paginator(current_page, page_size, datalist):
    if page_size != '-1':
        paginator_data = Paginator(datalist, page_size)
        try:
            data = paginator_data.page(current_page)
        except PageNotAnInteger:
            data = paginator_data.page(1)
        except InvalidPage:
            logErr.info(InvalidPage)
            return None
        data = serializers.serialize("json", data)
        return data
    data = serializers.serialize("json", datalist)
    return data


def create_sql(request):
    host = request.POST.get('host')
    user = request.POST.get('user')
    password = request.POST.get('password')
    db_name = request.POST.get('dbName')
    sql_type = request.POST.get('sqlType')
    mark = request.POST.get('mark')
    founder = request.POST.get('founder')
    port = request.POST.get('port') or None
    encoding = request.POST.get('encoding') or None
    link_test = request.POST.get('linkTest') or None
    try:
        SqlDispose.objects.create(host=host, user=user, password=password, dbName=db_name, sqlType=sql_type,
                                  mark=mark, founder=founder, port=port, encoding=encoding,
                                  linkTest=link_test)
        logInf.info('SqlDispose新增成功')
        return True
    except ValueError as e:
        logErr.info(e)
        return False
