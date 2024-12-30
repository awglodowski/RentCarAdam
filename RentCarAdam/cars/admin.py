from django.contrib import admin
from cars.models import Car, Reservation

# Register your models here.


class CarsAdmin(admin.ModelAdmin):
    list_display = ["id", "make", "model", "is_reserved"]
    fields = ["make", "model"]
    readonly_fields = ["is_reserved"]

admin.site.register(Car)
admin.site.register(Reservation)