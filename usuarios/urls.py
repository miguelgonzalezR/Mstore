from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lista_us/', login_required(lisus.as_view()), name='listaus'),
    path('agr_us/', login_required(resus.as_view()), name='agrus'),
    path('usuarios/<int:pk>/', login_required(elius), name='elu'),
    path('pke/<int:pk>/', login_required(idp), name='pke'),
    path('usuarios/e/<pk>/', login_required(usu_eli), name='elus'),
    path('usuarios/e/<pk>', login_required(used.as_view()), name='ediu'),
    path('mesaje/', mesaje, name='mesaje'),

]



