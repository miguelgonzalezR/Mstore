"""Mstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from usuarios.views import Login, logoutu
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy



urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include(('usuarios.urls', 'usuarios'))),
    path('admin/', admin.site.urls),
    path('accounts/login/',Login.as_view(), name='login'),
    path('logout/', login_required(logoutu), name='logout'),
    url(r'^cart/', include(('cart.urls', 'cart'))),
    url(r'^coupons/', include(('coupons.urls', 'coupons'))),
    url(r'^orders/', include(('orders.urls', 'orders'))),
    url(r'^', include(('shop.urls', 'shop'))),
    path('reset/password_reset', PasswordResetView.as_view(template_name ='contra/recup.html', email_template_name="contra/conem.html"), name='password_reset'),
    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name ="contra/men.html"), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='contra/escon.html'), name='password_reset_confirm'),
    url(r'^reset/done', PasswordResetCompleteView.as_view( template_name ='contra/incon.html'), name='password_reset_complete'),

]
