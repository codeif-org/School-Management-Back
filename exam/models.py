from django.db import models
from teacher.models import teacher, classSection, subject
from student.models import student

# Create your models here.
class exam(models.Model):
    # teacher = models.ForeignKey(teacher, on_delete=models.PROTECT)
    # classSection = models.ForeignKey(classSection, on_delete=models.PROTECT)
    # subject = models.ForeignKey(subject, on_delete=models.PROTECT)
    date = models.DateField(auto_now=True)
    name = models.CharField(max_length=100)
    max_marks = models.IntegerField()
    ms = models.BooleanField()

class ExamHeldSubject(models.Model):
    exam = models.ForeignKey(exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(subject, on_delete=models.CASCADE)
    
class score(models.Model):
    exam_held = models.ForeignKey(ExamHeldSubject, on_delete=models.CASCADE)
    stu = models.ForeignKey(student, on_delete=models.CASCADE)
    score = models.IntegerField()

        