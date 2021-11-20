from django.shortcuts import render, redirect
from .models import notice, receiver
from teacher.models import classSection, teacher, subject
from student.models import student
from superadmin.models import SuperAdmin, school
# Create your views here.

def showNotice(request):
    try:
        teacherobj = teacher.objects.get(user = request.user)
        school = teacherobj.school
    except:
        admin = SuperAdmin.objects.get(user = request.user)
        school = admin.school
    # classobj = classSection.objects.get(teacher = teacherobj)
    receivers = receiver.objects.filter(posted_by = request.user)
    return render(request, 'addNotice.html', {'receivers': receivers, 'school': school})

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
    return render(request, 'createNotice.html', {'classes': classes, 'school': school_object})

    
    

def studentNotice(request):
    studentobj = student.objects.get(user = request.user)
    print(studentobj.Class.id)
    classobj = classSection.objects.get(id = studentobj.Class.id)
    notices = receiver.objects.filter(receiver = classobj)
    print(notices)
    return render(request, 'notice.html', {'notices': notices, 'student': studentobj})
