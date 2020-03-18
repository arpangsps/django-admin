from django.db import models
from django.contrib.auth.models import User


class user_details(models.Model):
    phone_number = models.IntegerField(max_length = 10)
    role = models.CharField(max_length = 5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class user_details_2(models.Model):
    gender = models.CharField(max_length = 1, default = '')
    city = models.CharField(max_length = 15, default = '')


