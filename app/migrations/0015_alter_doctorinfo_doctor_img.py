# Generated by Django 3.2.6 on 2022-02-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_doctorinfo_doctor_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='doctor_img',
            field=models.ImageField(blank=True, default='new.jpg', upload_to='doctorimg'),
            preserve_default=False,
        ),
    ]
