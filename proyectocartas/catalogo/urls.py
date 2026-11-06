from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from .views import VendedorViewSet

router = DefaultRouter()
router.register(r'vendedores', VendedorViewSet, basename='vendedor')

urlpatterns = router.urls + [
    path('cartas/', views.obtener_cartas, name='obtener_cartas'),
    path('cartas/crear/', views.crear_cartas, name='crear_cartas'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
]