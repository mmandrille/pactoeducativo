# Generated by Django 2.0.5 on 2018-06-13 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, 'Documentos Pacto 2018'), (2, 'Antecedente')], default=1)),
                ('nombre', models.CharField(max_length=200, verbose_name='Titulo')),
                ('descripcion', models.TextField()),
                ('portada', models.FileField(default='/archivos/defaults/noimage.gif', upload_to='portadas/')),
                ('archivo', models.FileField(upload_to='')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de Publicacion')),
            ],
        ),
    ]