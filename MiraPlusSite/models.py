from django.db import models


# Create your models here.
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    rut = models.IntegerField()
    d_verificador = models.CharField(max_length=1)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    num_telefono = models.IntegerField()
    password = models.CharField(max_length=80)
    rol = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Departamento(models.Model):
    num_departamento = models.IntegerField(primary_key=True)
    cant_habitaciones = models.IntegerField()
    cant_banios = models.IntegerField()
    cant_habitantes = models.IntegerField()
    propietario = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)

    def __str__(self):
        return f"Departamento {self.num_departamento}"


class Residente(models.Model):
    id_residente = models.AutoField(primary_key=True)
    tipo_residente = models.CharField(max_length=80)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    num_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"Residente {self.id_residente} - Departamento {self.num_departamento.num_departamento}"


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    monto = models.FloatField()
    estado = models.CharField(max_length=80)
    fecha_pago = models.DateField()
    periodo_pago = models.DateField()
    num_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pago {self.id_pago} - Departamento {self.num_departamento.num_departamento}"



class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    tipo_solicitud = models.CharField(max_length=80)
    titulo_solicitud = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=80)
    fecha_solicitud = models.DateField()
    id_residente = models.ForeignKey(Residente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Solicitud {self.id_solicitud} - Residente {self.id_residente.id_residente}"


class Quejas(models.Model):
    id_queja = models.AutoField(primary_key=True)
    titulo_queja = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    fecha_queja = models.DateField()
    id_residente = models.ForeignKey(Residente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Queja {self.id_queja} - Residente {self.id_residente.id_residente}"


class Personal(models.Model):
    id_personal = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=80)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Personal {self.id_personal} - Cargo {self.cargo}"
