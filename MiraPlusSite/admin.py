from django.contrib import admin
from .models import Usuario, Departamento, Residente, Pago,Deuda, Solicitud


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Departamento)
admin.site.register(Residente)
admin.site.register(Pago)
admin.site.register(Deuda)
admin.site.register(Solicitud)

