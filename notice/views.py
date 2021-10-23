from django.shortcuts import render
from .models import notice
from teacher.models import classSection
from student.models import student
# Create your views here.

def showNotice(request):
    notices = notice.objects.all()
    return render(request, 'addNotice.html', {'notices': notices})

def createNotice(request):
    classes = classSection.objects.all()
    students = student.objects.all()
    number = len(students)
    l = []
    for i in range(1, number+1):
        l.append(i)
    return render(request, 'createNotice.html', {'classes': classes, 'students': students, 'l': l})