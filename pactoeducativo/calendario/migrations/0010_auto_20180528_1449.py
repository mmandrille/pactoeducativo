# Generated by Django 2.0.3 on 2018-05-28 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0009_auto_20180528_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 28, 14, 49, 28, 819648), verbose_name='Fecha de fin del Evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 28, 14, 49, 28, 819553), verbose_name='Fecha del Evento'),
        ),
    ]