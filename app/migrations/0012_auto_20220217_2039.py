# Generated by Django 3.2.6 on 2022-02-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_doctorinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='doctor_img',
            field=models.ImageField(null=True, upload_to='doctorimg'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='new_patient_fee',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='old_patient_fee',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='report_checking_fee',
            field=models.IntegerField(blank=True),
        ),
    ]
