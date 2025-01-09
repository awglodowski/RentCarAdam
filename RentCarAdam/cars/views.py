from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.timezone import now
from cars.filters import CarFilter
from cars.forms import ReservationForm
from cars.models import Car, Reservation
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from django_filters.views import FilterView

# Create your views here.

class CarsListView(FilterView, ListView):
    model = Car
    template_name = "cars_list.html"
    filterset_class = CarFilter

    # def get_queryset(self):
    #     # Fetch all cars, regardless of reservations
    #     return Car.objects.all()

    # def get_queryset(self):
    #     qs = Car.objects.filter(reservations__isnull=True)
    #     return qs

class CarsDetailView(DetailView):
    model = Car
    template_name = "cars_detail.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["form"] = ReservationForm()
        return context

# @csrf_protect
# def create_reservation(request, pk):
#     if request.method == "POST" and request.user.is_authenticated:
#         form = ReservationForm(request.POST)
#         car = get_object_or_404(Car, pk=pk)
#         if form.is_valid():
#             start_date = form.cleaned_data["start_date"]
#             end_date = form.cleaned_data["end_date"]
#             if start_date > end_date:
#                 start_date, end_date = end_date, start_date
#             if not car.is_selected_days_reserved(start_date, end_date):
#                 Reservation.objects.create(
#                     car=car,
#                     user=request.user,
#                     start_date=start_date,
#                     end_date=end_date,
#                 )
#                 # TODO redirect do profilu
#         else:
#             return render(request, "cars_detail.html", {"object": car, "form":form})
#     return redirect("cars-list")





@csrf_protect
def create_reservation(request, pk):
    if request.method == "POST" and request.user.is_authenticated:
        form = ReservationForm(request.POST)
        car = get_object_or_404(Car, pk=pk)

        if form.is_valid():
            start_date = form.cleaned_data["start_date"]
            end_date = form.cleaned_data["end_date"]

            # Ensure start_date is before end_date
            if start_date > end_date:
                #start_date, end_date = end_date, start_date
                messages.error(
                        request, "Start date is after the end date. Please correct the dates."
                    )
                return render(request, "cars_detail.html", {"object": car, "form": form})


            # Check if car is available for the selected dates
            if not car.is_selected_days_reserved(start_date, end_date):

                # Calculate total cost
                days_reserved = (end_date - start_date).days + 1
                total_cost = days_reserved * car.price_per_day

                # Create reservation
                Reservation.objects.create(
                    car=car,
                    user=request.user,
                    start_date=start_date,
                    end_date=end_date,
                )
                messages.success(
                    request,
                    f"Reservation created successfully! Thank you for placing your order. "
                    f"Total cost of your reservation will be {total_cost}."
                )

                #return redirect("cars-list")
            else:
                messages.error(request, "The car is already reserved for the selected dates.")
        else:
            messages.error(request, "Invalid reservation form data.")

        return render(request, "cars_detail.html", {"object": car, "form": form})

    #return redirect("cars-list")
