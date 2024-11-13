from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_deudas_pendientes/<int:depto_id>/', views.get_deudas_pendientes, name='get_deudas'),
    path('pagar_gasto_comun/', views.pagar_gasto_comun, name='pagar_gasto_comun')
]