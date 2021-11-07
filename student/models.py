from django.db import models
from django.contrib.auth.models import User
# from superadmin.models import school

# Create your models here.
class student(models.Model):
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    # dob = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    fathername = models.CharField(max_length=70)
    mothername = models.CharField(max_length=70)
    fatherphone = models.IntegerField()
    fatheremail = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200)
    add_no = models.CharField(max_length=50, blank=True, null=True)
    roll_no = models.IntegerField()
    Class = models.ForeignKey('teacher.classSection', on_delete=models.PROTECT)
    school = models.ForeignKey('superadmin.school', on_delete=models.PROTECT)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=50, blank=True, null=True)