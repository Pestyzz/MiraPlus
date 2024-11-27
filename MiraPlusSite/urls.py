from django.urls import path
from MiraPlusSite.view import pago_view
from MiraPlusSite.controller import pago_controller
from . import views

urlpatterns = [
    path('', pago_view.index, name='index'),
    path('get_deudas_pendientes/<int:depto_id>/', views.get_deudas_pendientes, name='get_deudas'),
    path('pagar_gasto_comun/', pago_controller.pagar_gasto_comun, name='pagar_gasto_comun')
]