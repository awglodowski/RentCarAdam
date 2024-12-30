from django.shortcuts import render

# Create your views here.
# STWORZYC PROFIL UZYTKOWNIKA (DetailView)
# Podlaczyc urls
# stworzyc w folderze management folder templates, a w nim user_detail.html
# dodac do contextu w widoku wszystkie rezerwacje uzytkownika (przyszle)
# dodac przekierowanie po stworzeniu rezerwacji na profil uzytkownika
from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView

from cars.models import Reservation
from management.models import User
from django.utils.timezone import now


# Create your views here.
# STWORZYC PROFIL UZYTKOWNIKA (DetailView) check
# Podlaczyc urls check
# stworzyc w folderze management folder templates, a w nim user_detail.html check
# dodac do contextu w widoku wszystkie rezerwacje uzytkownika (przyszle) check
# dodac przekierowanie po stworzeniu rezerwacji na profil uzytkownika


class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["reservations"] = Reservation.objects.filter(user_id=self.object.id, start_date__gte=now())
        return context
