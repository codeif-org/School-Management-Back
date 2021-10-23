from django.db import models
from teacher.models import teacher
# Create your models here.

class notice(models.Model):
        user = models.ForeignKey(teacher, on_delete=models.PROTECT, null = False, blank = False, default = '')
        classes = models.CharField(max_length=200)
        students = models.CharField(max_length=2000)
        topic = models.CharField(max_length=200)
        desc = models.CharField(max_length=2000)
        date = models.DateTimeField(auto_now=True)