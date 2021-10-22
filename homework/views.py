from django.shortcuts import render
from teacher.models import classSection, teacher, subject
# Create your views here.

def homeworkTeacher(request):
    return render(request, 'homeworkTeacher.html')

def createHomework(request):
    teacherobj = teacher.objects.get(user = request.user)
    schoolobj = teacherobj.school
    classes = subject.objects.filter(teacher = request.user.id)
    return render(request, 'createHomework.html', {'classes': classes})