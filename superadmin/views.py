from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from student.models import student
import superadmin
from teacher.models import classSection, teacher,subject
from .models import SuperAdmin, school
import json

# Create your views here.
def adminhome(request):
    # print(request.user)
    super_admin = SuperAdmin.objects.get(user = request.user)
    school_id = super_admin.school.id
    schoolobj = super_admin.school
    return render(request, 'adminhome.html', {'school_id': school_id, 'school': schoolobj})

def addTeacher(request):
    super_admin = SuperAdmin.objects.get(user = request.user)
    school = super_admin.school
    if request.method == "POST":
        fname = request.POST['fname']
        try:
            mname = request.POST['mname']
        except:
            mname = ''
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        try:
            address = request.POST['address']
        except:
            address = ''
        u = User.objects.create_user(username = fname, password = "12345678")
        u.save()
        admin = request.user
        superadmin = SuperAdmin.objects.get(user = admin)
        schoolobj = school.objects.get(school = superadmin.school.school)
        t = teacher(fname = fname, mname = mname, lname = lname, email = email, phone = phone, user = u, school = schoolobj)
        t.save()
        return redirect('superadmin:adminhome')
    return render(request, 'addTeacher.html', {'school': school})

def addStudent(request):
    super_admin = SuperAdmin.objects.get(user = request.user)
    school = super_admin.school
    if request.method == "POST":
        ad_no = request.POST['ad-no']
        fname = request.POST['fname']
        try:
            mname = request.POST['mname']
        except:
            mname = ''
        lname = request.POST['lname']
        Class = request.POST['class']
        c=""
        s=""
        for i in Class:
            if i>'0' and i<'9':
                c+=i
            else:
                s+=i
        classobj = classSection.objects.get(Class = c, section = s)
        email = request.POST['email']
        roll = request.POST['roll']
        dob = request.POST['dob']
        fathername = request.POST['fathname']
        mothername = request.POST['motname']
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        try:
            fatheremail = request.POST['pemail']
        except:
            fatheremail = ''
        try:
            address = request.POST['address']
        except:
            address = ''
        u = User.objects.create_user(username = fname, password = "12345678")
        u.save()
        admin = request.user
        superadmin = SuperAdmin.objects.get(user = admin)
        schoolobj = school.objects.get(school = superadmin.school.school)
        s = student(fname = fname, mname = mname, lname = lname, ad_no = ad_no, roll_no = roll, Class = classobj, email = email, dob = dob, fathername = fathername, mothername = mothername, phone = phone1, fatherphone = phone2, fatheremail = fatheremail, address = address, user = u, school = schoolobj)
        s.save()
        return redirect('superadmin:adminhome')
    return render(request, 'addStudents.html', {'school': school})

def students(request):
    admin = SuperAdmin.objects.get(user = request.user)
    school = admin.school
    students = student.objects.filter(school = admin.school)
    classes = classSection.objects.filter(teacher__in = teacher.objects.filter(school=admin.school))
    # sort(classes)
    return render(request, 'students.html', {'students': students, 'classes': classes})

def teachers(request):
    admin = SuperAdmin.objects.get(user = request.user)
    school = admin.school
    teachers = teacher.objects.filter(school = admin.school)
    classes = classSection.objects.filter(teacher__in = teacher.objects.filter(school = admin.school))
    return render(request, 'teachers.html', {'teachers': teachers, 'classes': classes, 'school': school})

def info(request):
    super_admin = SuperAdmin.objects.get(user = request.user)
    school = super_admin.school
    return render(request, 'schoolInfo.html', {'school': school})

def infoAPI(request):
    # print(request.user)
    # print(request.GET['user'])
    # user = request.GET['user']
    user = request.user
    # userobj = User.objects.get(username = user)
    try:
        schoolobj = SuperAdmin.objects.get(user = user).school
    except 1:
        schoolobj = teacher.objects.get(user = user).school
    except 2:
        schoolobj = student.objects.get(user = user).school        
    school_dict = school.objects.filter(id = schoolobj.id).values()
    # print(school_dict)
    school_json = json.dumps(list(school_dict))      
    # print(school_json)  
    return HttpResponse(school_json, content_type = "application/json")

def classes(request):
    admin_obj = SuperAdmin.objects.get(user = request.user)
    school_obj = admin_obj.school
    teacher_qs = teacher.objects.filter(school = school_obj)
    class_qs = classSection.objects.filter(teacher__in = teacher_qs)
    print(class_qs) 
    # try:
    #     classTeacher = classSection.objects.get(teacher=request.user.id)
    # except:
    #     classTeacher = None
    # try:
    #     classes = subject.objects.filter(teacher=request.user.id)
    # except:
    #     classes = None
    # print(classTeacher)
    # print(classes)
    return render(request, 'classes.html', {'classes': class_qs})