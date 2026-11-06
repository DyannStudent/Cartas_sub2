from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import cartasViewSet
from .views import VendedorViewSet

router = DefaultRouter()
router.register(r'vendedores', VendedorViewSet, basename='vendedor')

router.register(r'cartas', cartasViewSet, basename='cartas')

router.register(r'clientes', views.ClienteViewSet, basename='cliente')

urlpatterns = [
    path('', include(router.urls)),
]
