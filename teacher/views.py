from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import teacher, classSection, subject
from student.models import student
from superadmin.models import school, SuperAdmin

from teacher.serializers import SubjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def teacherhome(request):
    username = request.user.username
    t = teacher.objects.get(user = request.user)
    s = t.school
    return render(request, 'home.html', {'school': s})


def addStudent(request, class_name):
    t = teacher.objects.get(user = request.user)
    school = t.school
    classobj = classSection.objects.get(teacher=request.user.id)
    students = student.objects.filter(Class=classobj)
    number = len(students)
    l = []
    for i in range(1, number+1):
        l.append(i)
    return render(request, 'addStudent.html', {'students': students, 'l': l, 'school': school})


def YourClasses(request):
    # class_var = []
    teacherobj = teacher.objects.get(user = request.user)
    school = teacherobj.school
    try:
        classTeacher = classSection.objects.get(teacher=request.user.id)
    except:
        classTeacher = None
    try:        
        classes = subject.objects.filter(teacher=request.user.id)
    except:
        classes = None    
    print(classTeacher)
    print(classes)
    return render(request, 'YourClasses.html', {'class': classTeacher, 'classes': classes, 'school': school})
    # except:
    #     return render(request, 'YourClasses.html', {'msg': 'You are not assigned to any class'})
    
    


def classStudentList(request, class_id):
    Class = classSection.objects.get(id=class_id)
    teacherobj = teacher.objects.get(user=request.user)
    schoolobj = teacherobj.school
    students = student.objects.filter(school = schoolobj, Class = Class)
    # number = len(students)
    # l = []
    # for i in range(1, number+1):
    #     l.append(i)
    return render(request, 'classStudentList.html', {'students': students, 'class': Class.Class})

def addStudents(request):
    if request.method=="POST":
        fname = request.POST['fname']
        try:
            mname = request.POST['mname']
        except:
            mname = ''
        lname = request.POST['lname']
        ad_no = request.POST['ad-no']
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
        Class = classSection.objects.get(teacher = teacher.objects.get(user = request.user))
        u = User.objects.create_user(username = fname, password = "12345678")
        u.save()
        t = teacher.objects.get(user = request.user)
        schoolobj = school.objects.get(school = t.school.school)
        s = student(fname = fname, mname = mname, lname = lname, ad_no = ad_no, roll_no = roll, Class = Class, email = email, dob = dob, fathername = fathername, mothername = mothername, phone = phone1, fatherphone = phone2, fatheremail = fatheremail, address = address, user = u, school = schoolobj)
        s.save()
        return redirect('teacher:teacherhome')
    return render(request, 'addStudentForm.html')


@api_view(["GET", "POST"])
def subjectAPI(request):
    print(request.GET)
    if request.method == "GET":
        if "class" in request.GET:
            try:
                schoolobj = SuperAdmin.objects.get(user = request.GET["user"]).school
                print(schoolobj)
                teacher_qs = teacher.objects.filter(school = schoolobj)
                print(teacher_qs)
                class_qs = classSection.objects.filter(teacher__in = teacher_qs, Class = request.GET["class"]).values()
                print(class_qs)
                cls = classSection.objects.get(id=request.GET["class"])
                sub = subject.objects.filter(Class=cls)
                serializer = SubjectSerializer(sub, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response({"msg": "Class not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"msg": "This is here inside subject API"})
