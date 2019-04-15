from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Day11(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ans1_1 = models.CharField(max_length=100)
    time = models.TimeField(auto_now=True)


class Day12(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ans1_2 = models.CharField(max_length=100)
    time = models.TimeField(auto_now=True)


class Day13(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ans1_3 = models.CharField(max_length=100)
    time = models.TimeField(auto_now=True)


