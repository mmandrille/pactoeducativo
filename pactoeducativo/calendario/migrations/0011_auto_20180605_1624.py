# Generated by Django 2.0.5 on 2018-06-05 19:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0010_auto_20180528_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de fin del Evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha del Evento'),
        ),
    ]
