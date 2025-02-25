# Generated by Django 5.0.6 on 2024-07-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_defaultuser_sexo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defaultuser',
            name='is_jefe',
        ),
        migrations.AlterField(
            model_name='defaultuser',
            name='Rol_de_usuario',
            field=models.CharField(choices=[('Decano', 'Decano'), ('Vice Decano', 'Vice Decano'), ('Rector', 'Rector'), ('Jefe de departamento', 'Jefe de departamento'), ('Profesor', 'Profesor')], max_length=30, null=True, verbose_name='Rol de usuario'),
        ),
        migrations.AlterField(
            model_name='defaultuser',
            name='sexo',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1, verbose_name='Sexo'),
        ),
    ]
