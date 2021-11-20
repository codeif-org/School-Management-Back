from django.shortcuts import render, redirect
from student.models import student
from teacher.models import classSection, teacher, subject
from .models import Homework, Student_Homework, HomeworkSubmission
# Create your views here.

def homeworkTeacher(request):
    t = teacher.objects.get(user = request.user)
    school = t.school
    subjects = subject.objects.filter(teacher = teacher.objects.get(user = request.user))
    classes = []
    for sub in subjects:
        classes.append(sub.Class)
    homeworks = []
    for Class in classes:
        student_homework = Student_Homework.objects.filter(Class = Class)
        for hw in student_homework:
            homeworks.append(hw)
    return render(request, 'homeworkTeacher.html', {'homeworks': homeworks, 'school': school})

def createHomework(request):
    teacherobj = teacher.objects.get(user = request.user)
    schoolobj = teacherobj.school
    classes = subject.objects.filter(teacher = teacherobj)
    if request.method == 'POST':
        Class = request.POST['Class']
        topic = request.POST['topic']
        desc = request.POST['description']
        due_date = request.POST['due-date']
        classobj = classSection.objects.get(id = Class)
        homework = Homework(topic = topic, desc = desc, due_date = due_date)
        homework.save()
        teacherobj = teacher.objects.get(user = request.user)
        subjectobj = subject.objects.get(teacher = teacherobj, Class = classobj)
        hw = Student_Homework(subject = subjectobj, homework = homework, Class = classobj)
        hw.save()
        return redirect('homework:homeworkTeacher')
    return render(request, 'createHomework.html', {'classes': classes, 'school': schoolobj})


def homeworkStudent(request, id):
    studentobj = student.objects.get(user = request.user)
    Class = studentobj.Class
    homeworks = Student_Homework.objects.filter(Class = Class)
    completed = HomeworkSubmission.objects.filter(student = student.objects.get(user = request.user))
    completed_homeworks = []
    for c in completed:
        completed_homeworks.append(c.homework)
    completed_ids = []
    for completed_homework in completed_homeworks:
        completed_ids.append(completed_homework.homework.id)
    if id == 1:
        submitted = True
        return render(request, 'homework.html', {'homeworks': completed_homeworks, 'submitted': submitted, 'completed': completed})
    due_homeworks = []     
    for hw in homeworks:
        if hw.homework.id not in completed_ids:
            due_homeworks.append(hw)
    submitted = False
    return render(request, 'homework.html', {'homeworks': due_homeworks, 'submitted': submitted, 'student': studentobj})

def submitHomework(request, homework_id):
    studentobj = student.objects.get(user = request.user)
    homeworkStudent = Student_Homework.objects.get(homework = Homework.objects.get(id = homework_id))
    homework_submission = ''
    submission = ''
    try:
        submission = HomeworkSubmission.objects.get(student = student.objects.get(user = request.user), homework = Student_Homework.objects.get(homework = Homework.objects.get(id = homework_id)))
        submitted = True
        return render(request, 'submitHomework.html', {'submitted': submitted, 'sub': submission, 'homework': homeworkStudent})
    except:
        submitted = False
    if request.method == "POST":
        stu = student.objects.get(user = request.user)
        homework = Student_Homework.objects.get(homework = Homework.objects.get(id = homework_id))
        sub_desc = request.POST['sub_desc']
        homework_submission = HomeworkSubmission(student = stu, homework = homework, sub_desc = sub_desc)
        homework_submission.save()
        return redirect('homework:homework', id = 1)
    return render(request, 'submitHomework.html', {'submitted': submitted, 'submission': homework_submission, 'sub': submission, 'homework': homeworkStudent, 'student': studentobj})

def homeworkList(request, homework_id):
    homework = Student_Homework.objects.get(homework = Homework.objects.get(id = homework_id))
    students = HomeworkSubmission.objects.filter(homework = homework)
    return render(request, 'classListHW.html', {'homework': homework, 'students': students})