from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage


# Create your views here.
def paginator(current_page, page_size, datalist):
    if page_size != '-1':
        paginator_data = Paginator(datalist, page_size)
        try:
            data = paginator_data.page(current_page)
        except PageNotAnInteger:
            data = paginator_data.page(1)
        except InvalidPage:
            return None
        data = serializers.serialize("json", data)
        return data
    data = serializers.serialize("json", datalist)
    return data
