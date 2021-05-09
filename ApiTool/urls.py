"""ApiTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from paramAnalysis.views import index
from user import apis as u_apis
from sqlDispose import apis as sql_apis

urlpatterns = [
    path('admin/', admin.site.urls),

    # user
    path('user/register', u_apis.register),
    path('user/login', u_apis.login),
    path('user/logout', u_apis.logout),
    path('user/del', u_apis.user_del),

    # paramAnalysis
    path('paramAnalysis/index', index),

    # sqlDispose
    path('sqlDispose/linkTest', sql_apis.link_test),
    path('sqlDispose/disposeData', sql_apis.dispose_data),
    path('sqlDispose/disposeAll', sql_apis.dispose_all),
    path('sqlDispose/insertSql', sql_apis.insert_sql),
]
