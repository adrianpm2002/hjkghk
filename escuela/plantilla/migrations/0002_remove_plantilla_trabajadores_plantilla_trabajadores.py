# Generated by Django 5.0.6 on 2024-07-01 20:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantilla',
            name='Trabajadores',
        ),
        migrations.AddField(
            model_name='plantilla',
            name='Trabajadores',
            field=models.ManyToManyField(related_name='trabajador', to=settings.AUTH_USER_MODEL),
        ),
    ]
