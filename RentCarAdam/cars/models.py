from django.db.models import Q
from django.utils.timezone import now
from django.db import models

from management.models import User

class Car(models.Model):
    MAKE_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('BMW', 'BMW'),
        ('Lexus', 'Lexus'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('Kia', 'Kia'),
        ('Nissan', 'Nissan'),
        ('Volkswagen', 'Volkswagen'),
        ('Tesla', 'Tesla'),
        ('Volvo', 'Volvo'),
    ]

    CATEGORY_CHOICES = [
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Sport', 'Sport'),
    ]

    make = models.CharField(verbose_name="Make", max_length=32, choices=MAKE_CHOICES)
    model = models.CharField(verbose_name="Model", max_length=32)
    category = models.CharField(verbose_name="Category", max_length=32, choices=CATEGORY_CHOICES)
    price_per_day = models.DecimalField(verbose_name="Price per day", max_digits=10, decimal_places=2, default=0.00,)


    # picture = models.ImageField(verbose_name="Zdjecie domku")
    # localization = models.

    def __str__(self):
        return f"id: {self.id} {self.make} {self.model} "

    @property
    def is_reserved(self):
        return self.reservations.all().exists()

    # lt - less than <
    # lte - less than equal <=
    # gt - greater than >
    # gte - greater than equal >=

    # | OR
    # & AND
    def is_selected_days_reserved(self, new_start_date, new_end_date):
        check = Car.get_selected_days_reserved_filter(new_start_date, new_end_date)
        return Car.objects.filter(check, id=self.id).exists()

    @staticmethod
    def get_selected_days_reserved_filter(new_start_date, new_end_date):
        first_check = Q(
            reservations__start_date__lt=new_start_date,
            reservations__end_date__gt=new_start_date,
        )
        second_check = Q(
            reservations__start_date__gte=new_start_date,
            reservations__end_date__lte=new_end_date,
        )
        third_check = Q(
            reservations__start_date__lt=new_end_date,
            reservations__end_date__gt=new_end_date,
        )
        return first_check | second_check | third_check

class Reservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT, related_name="reservations")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(verbose_name="Reservation start date")
    end_date = models.DateField(verbose_name="Reservation end date")

    def __str__(self):
        return f"Reservation {self.id} for Car {self.car}"