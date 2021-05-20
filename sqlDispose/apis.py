import logging

from common.http import render_json
from common import error

from .models import SqlDispose
from .logic import paginator, create_sql_from, update_sql_from, del_sql, link_test_sql

from .forms import SqlDisposeForm, UpdateSqlDisposeForm

logInf = logging.getLogger('inf')
logErr = logging.getLogger('err')


def dispose_data(request):
    if request.method != 'POST':
        logErr.info('请求方法不正确')
        return render_json(msg='请求方法不正确')
    current_page = request.POST.get('currentPage')
    page_size = request.POST.get('pageSize')
    datalist = SqlDispose.objects.all().filter(is_del='0')
    data = paginator(current_page, page_size, datalist)
    logInf.info('response data %s' % data)
    data = data.replace('null', 'None')
    return render_json(data=data)


def dispose_all(request):
    if request.method != 'POST':
        logErr.info('请求方法不正确')
        return render_json(msg='请求方法不正确')
    datalist = SqlDispose.objects.all().filter(is_del='0')
    total = datalist.__len__()
    return render_json(data={'total': total})


def insert_sql(request):
    if request.method != 'POST':
        logErr.info('请求方法不正确')
        return render_json(msg='请求方法不正确')
    form = SqlDisposeForm(request.POST)
    if form.is_valid():
        if create_sql_from(form.cleaned_data):
            return render_json(msg='新增成功')
    return render_json(code=error.INSERT_SQL_FAIL, msg=error.INSERT_SQL_FAIL_MSG)


def update_sql(request):
    if request.method != 'POST':
        logErr.info('请求方法不正确')
        return render_json(msg='请求方法不正确')
    form = UpdateSqlDisposeForm(request.POST)
    if form.is_valid():
        if update_sql_from(request.POST):
            return render_json(msg='更新成功')
    return render_json(msg='更新失败')


def delete_sql(request):
    if request.method != 'POST':
        logErr.info('请求方法不正确')
        return render_json(msg='请求方法不正确')
    if del_sql(request.POST):
        return render_json(msg='删除成功')
    return render_json(msg='删除失败')


def link_test(request):
    if request.method != 'POST':
        logErr.info('请求方法不正确')
        return render_json(msg='请求方法不正确')
    if link_test_sql(request.POST):
        return render_json(msg='数据库连接成功')
    return render_json(msg='数据库连接失败')
