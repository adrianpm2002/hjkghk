# Generated by Django 5.0.6 on 2024-06-22 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividad', '0004_alter_actividad_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='Clasificacion',
            field=models.CharField(choices=[('General', 'General'), ('Principal', 'Principal')], max_length=100),
        ),
    ]
