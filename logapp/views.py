from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from superadmin.models import SuperAdmin
from teacher.models import teacher
from student.models import student
from teacher.views import teacherhome
from student.views import studenthome
# Create your views here.

#below decorator will redirect authenticated users to their respective dashboard.
def login_excluded():
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                try:
                    t = teacher.objects.get(user = request.user)
                    return redirect('teacher:teacherhome')
                except:
                    try:
                        s = student.objects.get(user = request.user)
                        return redirect('student:studenthome')
                    except:
                        a = SuperAdmin.objects.get(user = request.user)
                        return redirect('superadmin:adminhome') 
            return view_method(request, *args, **kwargs)
        return _arguments_wrapper
    return _method_wrapper

@login_excluded()
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # print(request.user)
            try:
                t = teacher.objects.get(user = request.user)
                return redirect('teacher:teacherhome')
            except:
                try:
                    s = student.objects.get(user = request.user)
                    return redirect('student:studenthome')
                except:
                    a = SuperAdmin.objects.get(user = request.user)
                    return redirect('superadmin:adminhome')
        else:
            redirect('login')
    return render(request, 'login.html')

def logout(request):
    current_user = request.user
    auth.logout(request)
    return redirect('login')