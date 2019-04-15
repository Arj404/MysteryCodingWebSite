from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Day11(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    ans = models.CharField(max_length=100, default=0)
    time = models.TimeField(auto_now=True)

class Day(models.Model):
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, default=0)

class Day12(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=0)
    ans1_2 = models.CharField(max_length=100, default=0)
    time = models.TimeField(auto_now=True)


class Day13(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=0)
    ans1_3 = models.CharField(max_length=100, default=0)
    time = models.TimeField(auto_now=True)


