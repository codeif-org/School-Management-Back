from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from student.models import student

# Create your models here.
class teacher(models.Model):
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField()
    phone = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    school = models.ForeignKey('superadmin.school', on_delete=models.PROTECT)
    # username = models.CharField(max_length=50, blank=False, null=False)

class classSection(models.Model):
    Class = models.IntegerField()
    section = models.CharField(max_length=50)
    teacher = models.OneToOneField(teacher, on_delete=models.PROTECT)

class subject(models.Model):
    subject = models.CharField(max_length=50)
    Class = models.ForeignKey(classSection, on_delete=models.PROTECT)
    teacher = models.ForeignKey(teacher, on_delete=models.PROTECT)