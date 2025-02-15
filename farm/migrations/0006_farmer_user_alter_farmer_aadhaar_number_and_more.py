# Generated by Django 5.1.6 on 2025-02-13 15:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0005_alter_farmer_full_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='user',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='aadhaar_number',
            field=models.CharField(default=True, max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='date_of_birth',
            field=models.DateField(auto_created=True, default=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='mobile_number',
            field=models.CharField(default=True, max_length=10, unique=True),
        ),
    ]
