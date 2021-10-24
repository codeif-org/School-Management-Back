from django.shortcuts import render, redirect
from student.models import student
from teacher.models import classSection, teacher, subject
from .models import Homework, Student_Homework
# Create your views here.

def homeworkTeacher(request):
    subjects = subject.objects.filter(teacher = teacher.objects.get(user = request.user))
    classes = []
    for sub in subjects:
        classes.append(sub.Class)
    homeworks = []
    for Class in classes:
        student_homework = Student_Homework.objects.filter(Class = Class)
        for hw in student_homework:
            homeworks.append(hw)
    return render(request, 'homeworkTeacher.html', {'homeworks': homeworks})

def createHomework(request):
    teacherobj = teacher.objects.get(user = request.user)
    schoolobj = teacherobj.school
    classes = subject.objects.filter(teacher = teacherobj)
    if request.method == 'POST':
        Class = request.POST['Class']
        topic = request.POST['topic']
        desc = request.POST['description']
        due_date = request.POST['due-date']
        classobj = classSection.objects.get(Class = Class)
        homework = Homework(topic = topic, desc = desc, due_date = due_date)
        homework.save()
        teacherobj = teacher.objects.get(user = request.user)
        subjectobj = subject.objects.get(teacher = teacherobj, Class = classobj)
        hw = Student_Homework(subject = subjectobj, homework = homework, Class = classobj)
        hw.save()
        return redirect('homework:homeworkTeacher')
    return render(request, 'createHomework.html', {'classes': classes})


def homeworkStudent(request):
    studentobj = student.objects.get(user = request.user)
    Class = studentobj.Class
    homeworks = Student_Homework.objects.filter(Class = Class)
    
    # subjects = []
    # for hw in homeworks:
    #     cs = classSection.objects.get(Class = studentobj.Class.Class)
    #     subjectobj = subject.objects.get(Class = cs, teacher = teacher.objects.get(user = hw.user))
    #     subjects.append(subjectobj.subject)
    # return render(request, 'homework.html', {'homeworks': homeworks, 'student': studentobj, 'subjects': subjects})
    return render(request, 'homework.html', {'homeworks': homeworks})