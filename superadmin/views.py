from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from student.models import student
from teacher.models import classSection, teacher
from .models import SuperAdmin, school

# Create your views here.
def adminhome(request):
    return render(request, 'adminhome.html')

def addTeacher(request):
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
    return render(request, 'addTeacher.html')

def addStudent(request):
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
    return render(request, 'addStudents.html')