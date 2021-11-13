from django.http.response import HttpResponse
from django.shortcuts import render, redirect

import superadmin
from .models import notice, receiver
from teacher.models import classSection, teacher, subject
from student.models import student
from superadmin.models import SuperAdmin, school
# Create your views here.

def showNotice(request):
    # teacherobj = teacher.objects.get(user = request.user)
    # classobj = classSection.objects.get(teacher = teacherobj)
    receivers = receiver.objects.filter(posted_by = request.user)
    return render(request, 'addNotice.html', {'receivers': receivers})

def createNotice(request):
    try:
        teacherobj = teacher.objects.get(user = request.user)
        classes_teacher_obj = classSection.objects.filter(teacher = teacherobj)
        teacher_subject = subject.objects.filter(teacher = teacherobj)
        # print(classes_teacher_obj)
        classes = [classes_teacher_obj[0]]
        for sub in teacher_subject:
            classes.append(sub.Class)
        # print("classes list", classes)
    except:
        super_admin = SuperAdmin.objects.get(user = request.user)
        school_object = super_admin.school
        classes = classSection.objects.filter(teacher__in = teacher.objects.filter(school = school_object))
    if request.method == 'POST':
        print(request.POST)
        topic = request.POST['topic']
        desc = request.POST['desc']
        noticeobj = notice(topic = topic, desc = desc)
        noticeobj.save()
        allclasses = request.POST.getlist('checks')
        if 'all' in allclasses:
            for c in classes:
                receiverobj = receiver(note = noticeobj, receiver = c, posted_by = request.user)
                receiverobj.save()
        else:
            for c in allclasses:
                print(c)
                classobj = classSection.objects.get(id = c)
                receiverobj = receiver(note = noticeobj, receiver = classobj, posted_by = request.user)
                receiverobj.save()
        return redirect('notice:createNotice')    
    return render(request, 'createNotice.html', {'classes': classes})


def studentNotice(request):
    studentobj = student.objects.get(user = request.user)
    print(studentobj.Class.id)
    classobj = classSection.objects.get(id = studentobj.Class.id)
    notices = receiver.objects.filter(receiver = classobj)
    print(notices)
    return render(request, 'notice.html', {'notices': notices, 'student': studentobj})


def superAdminNotice(request, category):
    print(category)
    user = request.user
    if category == 'all':
        # print(user)
        superadminObj = SuperAdmin.objects.get(user = user)
        schoolobj = superadminObj.school
        # print(schoolobj)
        superadmin_qs = SuperAdmin.objects.filter(school = schoolobj)
        # print(superadmin_qs)
        # notice_qs = receiver.objects.filter(posted_by__in = superadmin_qs.user)
        notice_qs = []
        for superadmin in superadmin_qs:
            notice_q = receiver.objects.filter(posted_by = superadmin.user)
            # print(notice_q)
            # notice_qs.append(notice_q)
            try:
                if notice_q[0].note:
                    for item in notice_q:
                        notice_qs.append(item)
            except:
                print("no notice")
                pass  
        print(notice_qs)    
        return render(request, 'superNotice.html', {'receivers': notice_qs, 'superadmin': superadminObj})
    elif category == 'sent':
        superadminObj = SuperAdmin.objects.get(user = user)
        schoolobj = superadminObj.school
        superadmin_qs = SuperAdmin.objects.filter(school = schoolobj)
        
        notice_qs = receiver.objects.filter(posted_by = user)
        print(notice_qs)
        return render(request, 'superNotice.html', {'receivers': notice_qs, 'superadmin': superadminObj})
        
        