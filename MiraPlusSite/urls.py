from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/test', views.deuda_list, name='deuda_list')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)