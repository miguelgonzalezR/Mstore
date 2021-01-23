from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^admin/dorder/(?P<order_id>\d+)$', login_required(views.readdo), name='order_detail'),
    url(r'^public/dorder/(?P<order_id>\d+)$', views.redpd, name='order_detailp'),
    path('Ordenes', login_required(views.prolis), name='Ordenes'),
    path('Ordenes/e/<pk>', login_required(views.edor.as_view()), name='edior'),

]
