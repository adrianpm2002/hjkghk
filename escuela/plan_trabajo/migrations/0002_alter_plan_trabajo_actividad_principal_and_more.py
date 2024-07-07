# Generated by Django 5.0.6 on 2024-06-25 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividad', '0005_alter_actividad_clasificacion'),
        ('plan_trabajo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan_trabajo',
            name='actividad_principal',
            field=models.ForeignKey(limit_choices_to={'Clasificacion': 'Principal'}, on_delete=django.db.models.deletion.CASCADE, related_name='Principal', to='actividad.actividad'),
        ),
        migrations.AlterField(
            model_name='plan_trabajo',
            name='actividades_generales',
            field=models.ForeignKey(limit_choices_to={'Clasificacion': 'General'}, on_delete=django.db.models.deletion.CASCADE, related_name='General', to='actividad.actividad'),
        ),
    ]