# Generated by Django 5.0.6 on 2024-07-05 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area1',
            name='Nombre_del_area',
            field=models.CharField(max_length=200, verbose_name='Nombre'),
        ),
    ]
