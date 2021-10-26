from django.shortcuts import render
from teacher.models import teacher, classSection
from student.models import student
from attendance.models import attendance
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import attendanceSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import serializers, status
import datetime
# Create your views here.


@api_view(['POST', 'PATCH'])
def saveAttendance(request, student_id):
    print("123456789")
    stu = student.objects.get(id = student_id)
    print(stu.fname)
    if request.method == 'POST':
        request.data['student'] = stu.id
        attendance_serializer = attendanceSerializer(data=request.data)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return JsonResponse(attendance_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(attendance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        date = request.data['date']
        obj = attendance.objects.get(student = stu, date = date)
        attendance_serializer = attendanceSerializer(obj, data = request.data, partial = True)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return JsonResponse(attendance_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(attendance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def Attendance(request):
    user = request.user
    t = teacher.objects.get(username = user.username)
    Class = classSection.objects.get(teacher = t)
    students = student.objects.filter(school = t.school, Class = Class)
    number = len(students)
    l = []
    for i in range(1, number+1):
        l.append(i)
    return render(request, 'attendance.html', {'students': students, 'l': l})

def studentAttendance(request):
    return render(request, 'studentAttendance.html')