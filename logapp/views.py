from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from teacher.models import teacher
from student.models import student
from teacher.views import teacherhome
from student.views import studenthome
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            try:
                t = teacher.objects.get(username = username)
                return redirect('teacher:teacherhome')
            except:
                s = student.objects.get(username = username)
                return redirect('student:studenthome')
        else:
            redirect('login')
    return render(request, 'login.html')

def logout(request):
    current_user = request.user
    auth.logout(request)
    return redirect('/')