# Generated by Django 5.0.6 on 2024-06-26 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaultuser',
            name='sexo',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='', max_length=1),
            preserve_default=False,
        ),
    ]
