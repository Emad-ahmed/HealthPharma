# Generated by Django 3.2.6 on 2022-02-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20220212_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cattype',
            field=models.CharField(default='Tablet', max_length=100),
        ),
    ]
