# Generated by Django 5.0.6 on 2024-11-10 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('num_departamento', models.IntegerField(primary_key=True, serialize=False)),
                ('cant_habitaciones', models.IntegerField()),
                ('cant_banios', models.IntegerField()),
                ('cant_habitantes', models.IntegerField()),
                ('propietario', models.CharField(max_length=80)),
                ('estado', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.IntegerField()),
                ('d_verificador', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('num_telefono', models.IntegerField()),
                ('password', models.CharField(max_length=80)),
                ('rol', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id_residente', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_residente', models.CharField(max_length=80)),
                ('num_departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiraPlusSite.departamento')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiraPlusSite.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Quejas',
            fields=[
                ('id_queja', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_queja', models.CharField(max_length=80)),
                ('descripcion', models.CharField(max_length=80)),
                ('estado', models.CharField(max_length=80)),
                ('fecha_queja', models.DateField()),
                ('id_residente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiraPlusSite.residente')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('monto', models.FloatField()),
                ('estado', models.CharField(max_length=80)),
                ('fecha_pago', models.DateField()),
                ('id_residente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiraPlusSite.residente')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_solicitud', models.CharField(max_length=80)),
                ('titulo_solicitud', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=80)),
                ('fecha_solicitud', models.DateField()),
                ('id_residente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiraPlusSite.residente')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id_personal', models.AutoField(primary_key=True, serialize=False)),
                ('cargo', models.CharField(max_length=80)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiraPlusSite.usuario')),
            ],
        ),
    ]