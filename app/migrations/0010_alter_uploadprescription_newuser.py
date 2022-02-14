# Generated by Django 3.2.6 on 2022-02-14 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_uploadprescription_newuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadprescription',
            name='newuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]