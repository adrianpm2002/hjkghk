# Generated by Django 5.0.6 on 2024-06-24 22:59

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='informe_cumplimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('Fecha', models.DateField(default=datetime.date.today)),
                ('Total_tareas_planificadas', models.IntegerField(max_length=2)),
                ('Cumplidas', models.IntegerField(max_length=2)),
                ('Incumplidas', models.IntegerField(max_length=2)),
                ('Nuevas_incorporadas', models.IntegerField(max_length=2)),
                ('Modificadas', models.IntegerField(max_length=2)),
                ('Descripcion', models.TextField(verbose_name=1000)),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
