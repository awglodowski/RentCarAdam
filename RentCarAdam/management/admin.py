from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from management.models import User

# Register your models here.

admin.site.register(User, UserAdmin)