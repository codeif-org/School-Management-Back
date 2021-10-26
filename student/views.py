from django.shortcuts import render
from superadmin.models import school
from student.models import student
from teacher.models import classSection, subject
# Create your views here.

def studenthome(request):
    studentobj = student.objects.get(user = request.user)
    sub = subject.objects.filter(Class = studentobj.Class)
    return render(request, 'index.html', {'student': studentobj, 'sub': sub[0]})
