from django.shortcuts import render
from superadmin.models import school
from student.models import student
# Create your views here.

def studenthome(request):
    studentobj = student.objects.get(user = request.user)
    return render(request, 'index.html', {'student': studentobj})

def progress(request):
    return render(request, 'progress.html')
