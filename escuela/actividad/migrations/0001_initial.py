# Generated by Django 5.0.6 on 2024-06-12 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='plan_trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Autor', models.CharField(max_length=50)),
                ('Clasificacion', models.CharField(max_length=100)),
            ],
        ),
    ]
