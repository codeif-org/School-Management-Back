from django.db import models

from teacher.models import classSection, subject,  teacher
from student.models import student

# Create your models here.
class Homework(models.Model):
    topic = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    due_date = models.DateTimeField()
    date = models.DateTimeField(auto_now=True)

class Student_Homework(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    Class = models.ForeignKey(classSection, on_delete=models.CASCADE)