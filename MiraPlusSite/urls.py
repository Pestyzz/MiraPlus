from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('test', views.deuda_list, name='deuda_list')
]