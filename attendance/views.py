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


@api_view(['GET', 'POST', 'PATCH'])
def saveAttendance(request):
    print("123456789")
    # student_id = request.data['student']
    # stu = student.objects.get(id=student_id)
    print(request.GET)
    # print(stu.fname)
    if request.method == "GET":
        if "student" in request.GET:
            stu = request.GET["student"]
            att = attendance.objects.filter(student=stu)
            print(att)
            serializer = attendanceSerializer(att, many=True)
            return Response(serializer.data)
        return Response({"msg": "Add query parameter 'student' against URL"})

    if request.method == 'POST':
        # request.data['student'] = stu.id
        attendance_serializer = attendanceSerializer(data=request.data)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return Response(attendance_serializer.data, status=status.HTTP_201_CREATED)
        return Response(attendance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        date = request.data['date']
        stu = request.data['student']
        obj = attendance.objects.get(student=stu, date=date)
        attendance_serializer = attendanceSerializer(
            obj, data=request.data, partial=True)
        if attendance_serializer.is_valid():
            attendance_serializer.save()
            return Response(attendance_serializer.data, status=status.HTTP_201_CREATED)
        return Response(attendance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def Attendance(request):
    user = request.user
    t = teacher.objects.get(user=user)
    Class = classSection.objects.get(teacher=t)
    students = student.objects.filter(school=t.school, Class=Class)
    print(students)
    return render(request, 'attendance.html', {'students': students})
