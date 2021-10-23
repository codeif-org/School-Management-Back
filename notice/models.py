from django.db import models
from teacher.models import classSection
from student.models import student
# Create your models here.

class notice(models.Model):
        topic = models.CharField(max_length=200)
        desc = models.CharField(max_length=2000)
        date = models.DateTimeField(auto_now=True)

class receiver(models.Model):
        note = models.ForeignKey(notice, on_delete=models.PROTECT)
        receiver = models.ForeignKey(classSection, on_delete=models.PROTECT)