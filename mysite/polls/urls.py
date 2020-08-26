from django.urls import path

from . import views     # top level import

urlpatterns = [
    path('', views.index, name='index'),
    path('second', views.second_page, name='second'),
]

