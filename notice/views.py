from django.shortcuts import render, redirect
from .models import notice, receiver
from teacher.models import classSection, teacher
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
        classes = classSection.objects.filter(teacher = teacherobj)
    except:
        super_admin = SuperAdmin.objects.get(user = request.user)
        school_object = super_admin.school
        classes = classSection.objects.filter(teacher__in = teacher.objects.filter(school = school_object))
    if request.method == 'POST':
        topic = request.POST['topic']
        desc = request.POST['desc']
        noticeobj = notice(topic = topic, desc = desc)
        noticeobj.save()
        allclasses = request.POST.getlist('checks[]')
        if 'all' in allclasses:
            for c in classes:
                receiverobj = receiver(note = noticeobj, receiver = c, posted_by = request.user)
                receiverobj.save()
        else:
            for c in allclasses:
                classobj = classSection.objects.get(Class = c)
                receiverobj = receiver(note = noticeobj, receiver = classobj, posted_by = request.user)
                receiverobj.save()
        return redirect('notice:showNotice')
    return render(request, 'createNotice.html', {'classes': classes})

def studentNotice(request):
    studentobj = student.objects.get(user = request.user)
    classobj = classSection.objects.get(Class = studentobj.Class.Class)
    notices = receiver.objects.filter(receiver = classobj)
    return render(request, 'notice.html', {'notices': notices, 'student': studentobj})
