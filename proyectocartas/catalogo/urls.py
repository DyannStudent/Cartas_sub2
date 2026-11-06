from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='cliente')

urlpatterns = [
    path('cartas/', views.obtener_cartas, name='obtener_cartas'),
    path('cartas/crear/', views.crear_cartas, name='crear_cartas'),
    path('', include(router.urls)),
]
