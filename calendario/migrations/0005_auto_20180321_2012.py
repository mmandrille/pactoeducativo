# Generated by Django 2.0.2 on 2018-03-21 20:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0004_auto_20180321_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 20, 12, 0, 794699, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
