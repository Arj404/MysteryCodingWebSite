from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Day1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ans1_1 = models.CharField(max_length=100)
    ans2_1 = models.CharField(max_length=100)
    ans3_1 = models.CharField(max_length=100)

