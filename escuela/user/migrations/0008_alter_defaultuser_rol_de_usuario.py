# Generated by Django 5.0.6 on 2024-07-06 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_area_defaultuser_área'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultuser',
            name='Rol_de_usuario',
            field=models.CharField(choices=[('Decano', 'Decano'), ('Vice Decano', 'Vice Decano'), ('Rector', 'Rector'), ('Jefe de departamento', 'Jefe de departamento'), ('Profesor', 'Profesor')], default='Profesor', max_length=30, null=True, verbose_name='Rol de usuario'),
        ),
    ]
