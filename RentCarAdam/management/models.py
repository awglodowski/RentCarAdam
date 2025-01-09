from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User

class User(AbstractUser):
    pass

# class User(models.Model):
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	email = models.EmailField('User Email')
#
# 	def __str__(self):
# 		return self.first_name + ' ' + self.last_name