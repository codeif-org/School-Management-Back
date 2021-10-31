from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class school(models.Model):
    school = models.CharField(max_length=200, default='', blank=False, null=False)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    pin = models.IntegerField()
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    regno = models.CharField(max_length=100)

class SuperAdmin(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    school = models.ForeignKey(school, on_delete=models.PROTECT)
