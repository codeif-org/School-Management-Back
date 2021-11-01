from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import teacher, classSection, subject
from student.models import student
from superadmin.models import school

from teacher.serializers import SubjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def teacherhome(request):
    username = request.user.username
    t = teacher.objects.get(username=username)
    s = t.school
    return render(request, 'home.html', {'school': s})


def addStudent(request, class_name):
    classobj = classSection.objects.get(teacher=request.user.id)
    students = student.objects.filter(Class=classobj)
    number = len(students)
    l = []
    for i in range(1, number+1):
        l.append(i)
    return render(request, 'addStudent.html', {'students': students, 'l': l})


def YourClasses(request):
    classTeacher = classSection.objects.get(teacher=request.user.id)
    classes = subject.objects.filter(teacher=request.user.id)
    print(classes)
    return render(request, 'YourClasses.html', {'class': classTeacher.Class, 'classes': classes})


def classStudentList(request, class_id):
    Class = classSection.objects.get(id=class_id)
    teacherobj = teacher.objects.get(user=request.user)
    schoolobj = teacherobj.school
    students = student.objects.filter(school=schoolobj, Class=Class)
    # number = len(students)
    # l = []
    # for i in range(1, number+1):
    #     l.append(i)
    return render(request, 'classStudentList.html', {'students': students, 'class': Class.Class})


@api_view(["GET", "POST"])
def subjectAPI(request):
    print(request.GET)
    if request.method == "GET":
        if "class" in request.GET:
            try:
                cls = classSection.objects.get(id=request.GET["class"])
                sub = subject.objects.filter(Class=cls)
                serializer = SubjectSerializer(sub, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"msg": "Class not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg": "This is here inside subject API"})
