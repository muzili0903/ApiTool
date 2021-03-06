from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage

import logging

from sqlDispose.forms import UpdateSqlDisposeForm
from .models import SqlDispose
from common.sqlCommon import MySqlCom

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


def create_sql_from(data):
    host = data.get('host')
    user = data.get('user')
    password = data.get('password')
    db_name = data.get('dbName')
    sql_type = data.get('sqlType')
    mark = data.get('mark')
    founder = data.get('founder')
    port = data.get('port') or None
    encoding = data.get('encoding') or None
    link_test = data.get('linkTest') or None
    try:
        SqlDispose.objects.create(host=host, user=user, password=password, dbName=db_name, sqlType=sql_type,
                                  mark=mark, founder=founder, port=port, encoding=encoding,
                                  linkTest=link_test)
        return True
    except ValueError as e:
        logErr.info(e)
        return False


def update_sql_from(data):
    try:
        pk = data.get('id')
        sql = SqlDispose.objects.get(id=pk)
        form = UpdateSqlDisposeForm(instance=sql, data=data)
        form.save()
        logInf.info('SqlDispose更新成功')
        return True
    except ValueError as e:
        logErr.info(e)
        return False


def del_sql(data):
    try:
        pk = data.get('id')
        update_person = data.get('update_person')
        SqlDispose.objects.filter(id=pk).update(is_del=1, update_person=update_person)
        logInf.info('SqlDispose删除成功')
        return True
    except ValueError as e:
        logErr.info(e)
        return False


def link_test_sql(data):
    try:
        pk = data.get('id')
        sql = SqlDispose.objects.get(id=pk)
        host = sql.__dict__.get('host')
        user = sql.__dict__.get('user')
        password = sql.__dict__.get('password')
        database = sql.__dict__.get('dbName')
        port = sql.__dict__.get('port')
        charset = sql.__dict__.get('charset')
        db = MySqlCom(host=host, user=user, password=password, database=database, port=port,
                      charset=charset)
        if db.to_connected():
            sql.__dict__.update(linkTest=1)
            sql.save()
            return True
        else:
            sql.__dict__.update(linkTest=0)
            sql.save()
            return False
    except ValueError as e:
        logErr.info(e)
        return False
