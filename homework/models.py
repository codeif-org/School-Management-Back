from django.db import models

from teacher.models import classSection, subject,  teacher
from student.models import student

# Create your models here.
class homework(models.Model):
    user = models.ForeignKey(teacher, on_delete=models.PROTECT, null = False, blank = False, default = '')
    Class = models.CharField(max_length=50)
    topic = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    due_date = models.DateTimeField()
    date = models.DateTimeField(auto_now=True)