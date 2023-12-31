# Generated by Django 4.2.5 on 2023-11-06 09:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_employeeregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('address', models.TextField()),
                ('updated_date', models.DateTimeField(default=datetime.datetime.now)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/hospital/')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeRegistration',
        ),
        migrations.AddField(
            model_name='hospital',
            name='htype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.hospital_type'),
        ),
    ]
