# Generated by Django 4.2.5 on 2023-11-06 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_hospital_hospital_type_delete_employeeregistration_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hospital',
        ),
        migrations.DeleteModel(
            name='Hospital_Type',
        ),
    ]
