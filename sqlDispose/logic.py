from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage

import logging

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
