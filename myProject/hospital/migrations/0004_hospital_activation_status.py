# Generated by Django 4.2.5 on 2023-11-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_hospital_approval_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='activation_status',
            field=models.CharField(choices=[('A', 'Activated'), ('D', 'Deactivated')], default='D', max_length=1),
        ),
    ]
