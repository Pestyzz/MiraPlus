# Generated by Django 5.0.6 on 2024-11-12 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiraPlusSite', '0002_remove_pago_id_residente_remove_usuario_rol_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiraPlusSite.usuario'),
        ),
    ]