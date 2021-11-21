from django.http.response import HttpResponse
from django.shortcuts import render, redirect

import superadmin
from .models import notice, receiver
from teacher.models import classSection, teacher, subject
from student.models import student
from superadmin.models import SuperAdmin, school
from django.contrib.auth.models import User
# Create your views here.

def teacherNotice(request, category):
    if category == 'all':
        # teacherobj = teacher.objects.get(user = request.user)
        # classobj = classSection.objects.get(teacher = teacherobj)
        schoolobj = teacher.objects.get(user = request.user).school
        superadmin_qs = SuperAdmin.objects.filter(school = schoolobj)
        notice_qs = []
        for superadmin in superadmin_qs:
            notice_q = notice.objects.filter(posted_by = superadmin.user).values()
            print(notice_q)
            for item in notice_q:
                notice_qs.append(item)
        print(notice_qs)   
        for notice_q in notice_qs:
            notice_q["receiver"] = receiver.objects.filter(note = notice_q["id"])
            notice_q["posted_by"] = User.objects.get(id = notice_q["posted_by_id"]).username
        print("last notice_qs: ", notice_qs)  
        notice_qs.reverse()     
        return render(request, 'teacherNotice.html', {'notices': notice_qs})
          
        
    elif category == 'sent':    
        notice_qs = notice.objects.filter(posted_by = request.user).values()
        print(notice_qs)
        for notice_q in notice_qs:
            notice_q["receiver"] = receiver.objects.filter(note = notice_q["id"])
        print("last notice_qs:  ", notice_qs)  
        notice_qs.reverse()  
        return render(request, 'teacherNotice.html', {'notices': notice_qs})

def createNotice(request):
    try:
        teacherobj = teacher.objects.get(user = request.user)
        school_object = teacherobj.school
        classes_teacher_obj = classSection.objects.filter(teacher = teacherobj)
        teacher_subject = subject.objects.filter(teacher = teacherobj)
        # print(classes_teacher_obj)
        classes = [classes_teacher_obj[0]]
        for sub in teacher_subject:
            classes.append(sub.Class)
        # print("classes list", classes)
        posting_by = "teacher"
    except:
        super_admin = SuperAdmin.objects.get(user = request.user)
        school_object = super_admin.school
        classes = classSection.objects.filter(teacher__in = teacher.objects.filter(school = school_object))
        posting_by = "superadmin"
    if request.method == 'POST':
        print(request.POST)
        topic = request.POST['topic']
        desc = request.POST['desc']
        noticeobj = notice(topic = topic, desc = desc, posted_by = request.user)
        noticeobj.save()
        allclasses = request.POST.getlist('checks')
        if 'all' in allclasses:
            for c in classes:
                receiverobj = receiver(note = noticeobj, receiver = c)
                receiverobj.save()
        else:
            for c in allclasses:
                print(c)
                classobj = classSection.objects.get(id = c)
                receiverobj = receiver(note = noticeobj, receiver = classobj)
                receiverobj.save()
        return redirect('notice:createNotice')    
    if posting_by == "teacher":
        return render(request, 'createNotice.html', {'classes': classes})
    elif posting_by == "superadmin":
        return render(request, 'superadmincreateNotice.html', {'classes': classes})


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
        superadmin_qs = SuperAdmin.objects.filter(school = schoolobj).exclude(user = user)
        # superadmin_qs.remove(superadminObj)
        print(type(superadmin_qs))
        # print(superadmin_qs)
        # notice_qs = receiver.objects.filter(posted_by__in = superadmin_qs.user)
        notice_qs = []
        for superadmin in superadmin_qs:
            notice_q = notice.objects.filter(posted_by = superadmin.user).values()
            print(notice_q)
            for item in notice_q:
                notice_qs.append(item) 
        print(notice_qs)
        for notice_q in notice_qs:
            notice_q["receiver"] = receiver.objects.filter(note = notice_q["id"])
            notice_q["posted_by"] = User.objects.get(id = notice_q["posted_by_id"]).username
        print("last notice_qs: ", notice_qs)      
        notice_qs.reverse()  
        return render(request, 'superNotice.html', {'notices': notice_qs, 'superadmin': superadminObj, 'category': category})
    elif category == 'sent':
        superadminObj = SuperAdmin.objects.get(user = user)
        schoolobj = superadminObj.school
        superadmin_qs = SuperAdmin.objects.filter(school = schoolobj)
        notice_qs = notice.objects.filter(posted_by = user).order_by("date").values()
        for notice_q in notice_qs:
            notice_q["receiver"] = receiver.objects.filter(note = notice_q["id"])
        # print(notice_qs)  
        notice_qs_1 = [item for item in notice_qs]
        notice_qs_1.reverse() 
        print("last ", notice_qs_1)
        return render(request, 'superNotice.html', {'notices': notice_qs_1, 'superadmin': superadminObj, 'category': category})
        
        