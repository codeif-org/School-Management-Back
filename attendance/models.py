from django.db import models
from student.models import student
# Create your models here.
class attendance(models.Model):
    date = models.DateField()
    student = models.ForeignKey(student, on_delete=models.PROTECT)
    present = models.BooleanField()