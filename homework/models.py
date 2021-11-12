from django.db import models
from student.models import student
from teacher.models import classSection, subject,  teacher

# Create your models here.
class Homework(models.Model):
    topic = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    due_date = models.DateTimeField()
    date = models.DateTimeField(auto_now=True)

class Student_Homework(models.Model):
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    Class = models.ForeignKey(classSection, on_delete=models.CASCADE)

class HomeworkSubmission(models.Model):
    homework = models.ForeignKey(Student_Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    sub_date = models.DateTimeField(auto_now=True)
    sub_desc = models.CharField(max_length=2000, blank=True, null=True)
