from django.conf.urls import url, include

from . import views
from .views import IndexView, AnyPageView, ListView, PageView


app_name = 'stuff'

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', AnyPageView.as_view()),
    url(r'^pages/$', views.ListView.as_view()),
    url(r'^pages/(?P<id>[0-9]+)/$', PageView.as_view()),
]

#Modelo en el que poder editar datos desde Admin

#Datos no venir de views, si no base de datos.
