from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listar_platos, name='listar_platos'),
    url(r'^apprestaurante/(?P<pk>[0-9]+)/$', views.detalle_menus,  name='detalle_platos'),
    url(r'^apprestaurante/nuevo/$', views.menu_nuevo, name='menu_nuevo'),
    ]
