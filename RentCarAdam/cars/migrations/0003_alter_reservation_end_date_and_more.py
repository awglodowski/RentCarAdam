# Generated by Django 5.1.4 on 2024-12-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_car_priceperday_car_price_per_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='end_date',
            field=models.DateField(verbose_name='Reservation end date'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_date',
            field=models.DateField(verbose_name='Reservation start date'),
        ),
    ]
