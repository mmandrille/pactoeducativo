# Generated by Django 2.0.3 on 2018-03-27 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foto',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Foto',
        ),
    ]