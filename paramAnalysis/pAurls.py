from django.urls import path

from paramAnalysis import views

urlpatterns = [
    path('index', views.index, name='index'),
]
