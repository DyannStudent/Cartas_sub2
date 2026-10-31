from django.urls import path
from . import views

urlpatterns = [
    path('cartas/', views.obtener_cartas, name='obtener_cartas'),
    path('cartas/crear/', views.crear_cartas, name='crear_cartas'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
]