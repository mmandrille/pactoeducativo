# Generated by Django 2.0.2 on 2018-03-21 20:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180321_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 21, 20, 14, 25, 755753, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
