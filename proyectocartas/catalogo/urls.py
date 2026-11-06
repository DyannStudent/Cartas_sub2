from django.urls import path, include
from . import views
from .views import cartasList, cartasDetail
from rest_framework.routers import DefaultRouter
from .views import cartasViewSet

router = DefaultRouter()
router.register(r'cartas', cartasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
]