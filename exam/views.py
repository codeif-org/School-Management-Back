from django.shortcuts import render, redirect
from .models import exam, score
from superadmin.models import school
from teacher.models import teacher, classSection, subject
from student.models import student
# Create your views here.

def teacherExamList(request):
    usr = request.user
    oteacher = teacher.objects.get(user=usr)
    subjects = subject.objects.filter(teacher=oteacher)
    # print(subjects)
    exam_lst = []
    for sub in subjects:
        # print(sub)
        oexam = exam.objects.filter(subject=sub)
        # print(oexam)
        # exam_lst.append(oexam)
        for iexam in oexam:
            exam_lst.append(iexam)
    # exam_lst.append(oexam[0])
    # exam_lst.append(oexam[1])    
    # exams = exam.objects.all()
    # print("exams: ", exams)
    # print(exam_lst)
    return render(request, 'teacherExamList.html', {'exam_lst':exam_lst})


def createExam(request):
    obj = request.user
    t = teacher.objects.get(username = obj.username)
    subjects = subject.objects.filter(teacher = t)
    classes = classSection.objects.filter(teacher = t)
    if request.method == "POST":
        c = request.POST['class']
        section = request.POST['section']
        cs = classSection.objects.get(Class = c, section = section)
        s = request.POST['subject']
        sub = subject.objects.get(subject = s)
        name = request.POST['exam']
        marks = request.POST['marks']
        date = request.POST['date']
        test = exam(teacher = t, classSection = cs, subject = sub, date = date, name = name, marks = marks)
        test.save()
        return redirect('teacherExamList')
    return render(request, 'createExam.html', {'classes': classes, 'subjects': subjects})

def marksEdit(request, id):
    test = exam.objects.get(id = id)
    obj = school.objects.get(school = test.teacher.school.school)
    students = student.objects.filter(school = obj, Class = test.classSection)
    return render(request, 'marksEdit.html', {'students': students, 'exam': test})