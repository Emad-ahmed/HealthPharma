# Generated by Django 3.2.6 on 2022-02-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20220217_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='specialist',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
