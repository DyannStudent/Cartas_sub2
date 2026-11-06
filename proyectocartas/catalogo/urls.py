from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views
from .views import VendedorViewSet

router = DefaultRouter()
router.register(r'vendedores', VendedorViewSet, basename='vendedor')

urlpatterns = router.urls + [
router.register(r'clientes', views.ClienteViewSet, basename='cliente')

urlpatterns = [
    path('cartas/', views.obtener_cartas, name='obtener_cartas'),
    path('cartas/crear/', views.crear_cartas, name='crear_cartas'),
    path('', include(router.urls)),
]
