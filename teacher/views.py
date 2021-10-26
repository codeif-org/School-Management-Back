from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import teacher, classSection, subject
from student.models import student
from superadmin.models import school
# Create your views here.

def teacherhome(request):
    username = request.user.username
    t = teacher.objects.get(username = username)
    s = t.school
    return render(request, 'home.html', {'school': s})



def addStudent(request, class_name):
    classobj = classSection.objects.get(teacher = request.user.id)
    students = student.objects.filter(Class = classobj)
    number = len(students)
    l = []
    for i in range(1, number+1):
        l.append(i)
    return render(request, 'addStudent.html', {'students': students, 'l': l})

def YourClasses(request):
    classTeacher = classSection.objects.get(teacher = request.user.id)
    classes = subject.objects.filter(teacher = request.user.id)
    print(classes)
    return render(request, 'YourClasses.html', {'class': classTeacher.Class, 'classes': classes})

def classStudentList(request, class_id):
    Class = classSection.objects.get(id = class_id)
    teacherobj = teacher.objects.get(user = request.user)
    schoolobj = teacherobj.school
    students = student.objects.filter(school = schoolobj, Class = Class)
    # number = len(students)
    # l = []
    # for i in range(1, number+1):
    #     l.append(i)
    return render(request, 'classStudentList.html', {'students': students, 'class': Class.Class})