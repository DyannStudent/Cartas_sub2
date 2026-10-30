from django.urls import path
from . import views

urlpatterns = [
    path('cartas/', views.obtener_cartas, name='obtener_cartas'),
    path('cartas/crear/', views.crear_cartas, name='crear_cartas'),
]