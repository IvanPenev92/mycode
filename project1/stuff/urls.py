from django.conf.urls import url
from .views import IndexView, AnyPageView


app_name = 'stuff'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', AnyPageView.as_view(), name='list'),
]

# Modelo en el que poder editar datos desde Admin

# Datos no venir de views, si no base de datos.
