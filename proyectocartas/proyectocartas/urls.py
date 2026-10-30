
from django.contrib import admin
from django.urls import path
from catalogo.views import listar_vendedores, crear_vendedor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vendedores/', listar_vendedores, name='listar_vendedores'),
    path('vendedores/crear/', crear_vendedor, name='crear_vendedor'),
    path('api/', include('catalogo.urls')),  
]
