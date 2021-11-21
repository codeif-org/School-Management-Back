from django.db import models
from student.models import student
# Create your models here.
class attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(student, on_delete=models.PROTECT)
    present = models.BooleanField()

class Leave(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=1000)
    date_from = models.DateField()
    date_to = models.DateField()