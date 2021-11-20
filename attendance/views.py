from django.shortcuts import render, redirect
from teacher.models import teacher, classSection
from student.models import student
from attendance.models import attendance, Leave


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import attendanceSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import serializers, status
import datetime
from datetime import date
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
    school = t.school
    try:
        Class = classSection.objects.get(teacher=t)
        students = student.objects.filter(school=t.school, Class=Class)
        today_date = date.today()
        leaveStudents = Leave.objects.filter(student__in = student.objects.filter(Class = Class))
        print(leaveStudents)
        lStudents = []
        for ls in leaveStudents:
            if today_date>=ls.date_from and today_date<=ls.date_to:
                lStudents.append(ls)
        print(lStudents)
        lid = []
        for l in lStudents:
            lid.append(l.student.id)
        return render(request, 'attendance.html', {'students': students, 'leaves': lStudents, 'leaveId': lid, 'school': school})
    except:
        return render(request, 'attendance.html', {'msg': True})


def studentAttendance(request):
    studentobj = student.objects.get(user = request.user)
    attendances = attendance.objects.filter(student = student.objects.get(user = request.user))
    attended = 0
    total_classes = attendances.count()
    for att in attendances:
        if att.present == True:
            attended = attended + 1
    missed = total_classes - attended
    percentage = (attended/total_classes)*100
    return render(request, 'studentAttendance.html', {'total_classes': total_classes, 'attended': attended, 'missed': missed, 'percentage': str(round(percentage, 2)), 'student': studentobj})

def applyLeave(request):
    studentobj = student.objects.get(user = request.user)
    if request.method == "POST":
        stu = student.objects.get(user = request.user)
        date_from = request.POST['date_from']
        date_to = request.POST['date_to']
        reason = request.POST['reason']
        leave = Leave(student = stu, date_from = date_from, date_to = date_to, reason = reason)
        leave.save()
        return redirect('student:studenthome')
    return render(request,'applyLeave.html', {'student': studentobj})