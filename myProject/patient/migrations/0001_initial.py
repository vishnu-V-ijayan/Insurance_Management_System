# Generated by Django 4.2.5 on 2023-11-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30, verbose_name="Patient's First Name")),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name="Patient's Last Name")),
                ('slug', models.SlugField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('O', 'OTHERS')], max_length=10)),
                ('dateofbirth', models.DateField()),
                ('mobile_number', models.CharField(max_length=10, verbose_name="Patient's Mobile Number")),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('profileimage', models.ImageField(upload_to='images/patient/')),
            ],
        ),
    ]
