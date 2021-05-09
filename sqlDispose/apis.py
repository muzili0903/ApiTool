import logging

from common.http import render_json
from common import error

from .models import SqlDispose
from .logic import paginator

logInf = logging.getLogger('inf')
logErr = logging.getLogger('err')


def dispose_data(request):
    if request.method != 'POST':
        logErr.info('请求方法不正确')
        return render_json(msg='请求方法不正确')
    current_page = request.POST.get('currentPage')
    page_size = request.POST.get('pageSize')
    datalist = SqlDispose.objects.all()
    data = paginator(current_page, page_size, datalist)
    logInf.info('response data %s' % data)
    return render_json(data=data)


def dispose_all(request):
    if request.method != 'POST':
        logErr.info('请求方法不正确')
        return render_json(msg='请求方法不正确')
    datalist = SqlDispose.objects.all()
    total = datalist.__len__()
    return render_json(data={'total': total})


def insert_sql(request):
    if request.method != 'POST':
        logErr.info('请求方法不正确')
        return render_json(msg='请求方法不正确')
    pass


def link_test(request):
    pass
