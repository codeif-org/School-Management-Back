from django.shortcuts import render
from student.models import student
from teacher.models import classSection, teacher, subject
from .models import homework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import homeworkSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import serializers, status
# Create your views here.

def homeworkTeacher(request):
    return render(request, 'homeworkTeacher.html')

def createHomework(request):
    teacherobj = teacher.objects.get(user = request.user)
    schoolobj = teacherobj.school
    classes = subject.objects.filter(teacher = request.user.id)
    return render(request, 'createHomework.html', {'classes': classes})

@api_view(['POST'])
def homeworkAPI(request):
    if request.method == 'POST':
        request.data['user'] = request.user
        homework_serializer = homeworkSerializer(data = request.data)
        if homework_serializer.is_valid():
            homework_serializer.save()
            return JsonResponse(homework_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(homework_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def homeworkStudent(request):
    studentobj = student.objects.get(user = request.user)
    homeworks = homework.objects.all()
    subjects = []
    for hw in homeworks:
        cs = classSection.objects.get(Class = studentobj.Class.Class)
        subjectobj = subject.objects.get(Class = cs, teacher = teacher.objects.get(user = hw.user))
        subjects.append(subjectobj.subject)
    return render(request, 'homework.html', {'homeworks': homeworks, 'student': studentobj, 'subjects': subjects})