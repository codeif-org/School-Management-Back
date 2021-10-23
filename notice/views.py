from django.shortcuts import render, redirect
from .models import notice, receiver
from teacher.models import classSection
from student.models import student
# Create your views here.

def showNotice(request):
    notices = notice.objects.all().order_by('-date')
    receivers = receiver.objects.all()
    return render(request, 'addNotice.html', {'notices': notices, 'receivers': receivers})

def createNotice(request):
    classes = classSection.objects.all()
    students = student.objects.all()
    number = len(students)
    l = []
    for i in range(1, number+1):
        l.append(i)
    if request.method == 'POST':
        topic = request.POST['topic']
        desc = request.POST['desc']
        noticeobj = notice(topic = topic, desc = desc)
        noticeobj.save()
        allclasses = request.POST.getlist('checks[]')
        print(allclasses)
        if 'all' in allclasses:
            for c in classes:
                receiverobj = receiver(note = noticeobj, receiver = c)
                receiverobj.save()
        else:
            for c in allclasses:
                classobj = classSection.objects.get(Class = c)
                receiverobj = receiver(note = noticeobj, receiver = classobj)
                receiverobj.save()
        return redirect('notice:showNotice')
    return render(request, 'createNotice.html', {'classes': classes, 'students': students, 'l': l})