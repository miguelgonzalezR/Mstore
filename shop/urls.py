from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.product_list, name="product_list"),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name="product_list_by_category"),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name="product_detail"),
    path('Categorias', login_required(views.catlis), name='Categorias'),
    path('Categoria/Agregar/',login_required(views.agcate.as_view()), name='AgregarCa'),
    path('Categoria/e/<pk>', login_required(views.edca.as_view()), name='edica'),

    path('Categoria/<int:pk>/', login_required(views.elica), name='elc'),
    path('pke/<int:pk>/', login_required(views.idca), name='pkec'),
    path('Categoria/e/<pk>/', login_required(views.cat_eli), name='elca'),

    path('Productos', login_required(views.prolis), name='Productos'),
    path('Productos/Agregar/',login_required(views.agcpro.as_view()), name='AgregarPro'),
    path('Productos/e/<pk>', login_required(views.edpro.as_view()), name='edipro'),

    path('Productos/<int:pk>/', login_required(views.elipro), name='elp'),
    path('pke/<int:pk>/', login_required(views.idpro), name='pkpro'),
    path('Productos/e/<pk>/', login_required(views.pro_eli), name='elpr'),
    path('Graficos/index', login_required(views.graf), name='home'),
    path('Ayuda', views.ayuda, name="Ayuda"),
    path('Sobren', views.nosob, name="Sobren"),

    
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

