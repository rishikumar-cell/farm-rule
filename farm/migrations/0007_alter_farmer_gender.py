# Generated by Django 5.1.6 on 2025-02-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0006_farmer_user_alter_farmer_aadhaar_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=True, max_length=30),
        ),
    ]
