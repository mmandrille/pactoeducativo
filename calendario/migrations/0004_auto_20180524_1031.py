# Generated by Django 2.0.5 on 2018-05-24 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0003_auto_20180523_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 24, 10, 31, 48, 389929), verbose_name='Fecha de fin del Evento'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 24, 10, 31, 48, 389911), verbose_name='Fecha del Evento'),
        ),
    ]
