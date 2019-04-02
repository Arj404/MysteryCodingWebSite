from django.db import models

# Create your models here.


class login(models.Model):
    name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
