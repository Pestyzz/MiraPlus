# Generated by Django 5.0.6 on 2024-11-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiraPlusSite', '0006_alter_departamento_estado_alter_pago_estado_deuda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='estado',
            field=models.CharField(choices=[('En Mantencion', 'En Mantencion'), ('Ocupado', 'Ocupado'), ('Disponible', 'Disponible')], max_length=80),
        ),
        migrations.AlterField(
            model_name='pago',
            name='estado',
            field=models.CharField(choices=[('Pago exitoso dentro del plazo', 'Pago exitoso dentro del plazo'), ('Pago exitoso fuera del plazo', 'Pago exitoso fuera del plazo'), ('Pago duplicado', 'Pago duplicado')], max_length=80),
        ),
    ]
