# Generated by Django 5.1.4 on 2025-01-04 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_rename_car_reservation_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]