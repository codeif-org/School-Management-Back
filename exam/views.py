from django.shortcuts import render, redirect, HttpResponse
from .models import exam, score, ExamHeldSubject
from superadmin.models import school
from teacher.models import teacher, classSection, subject
from student.models import student

# rest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from exam.serializers import ScoreSerializer

# Create your views here.


def teacherExamList(request):
    usr = request.user
    oteacher = teacher.objects.get(user=usr)
    subjects = subject.objects.filter(teacher=oteacher)
    # print(subjects)
    exam_lst = []
    for sub in subjects:
        # print(sub)
        oexam = ExamHeldSubject.objects.filter(subject=sub)
        print(oexam)
        # print(oexam)
        # exam_lst.append(oexam)
        for iexam in oexam:
            exam_lst.append(iexam)    
    # exam_lst.append(oexam[0])
    # exam_lst.append(oexam[1])
    # exams = exam.objects.all()
    # print("exams: ", exams)
    # print(exam_lst)
    return render(request, 'teacherExamList.html', {'exam_lst': exam_lst})

# sub: [subject ids array]


def createExam(request):
    obj = request.user
    t = teacher.objects.get(username=obj.username)
    subjects = subject.objects.filter(teacher=t)
    classes = classSection.objects.filter(teacher=t)
    if request.method == "POST":
        print(request.POST)
        print("subjects selected:", request.POST.getlist('sub'))
        exam_name = request.POST["exam_name"]
        max_marks = request.POST["max_marks"]
        sub_ids = request.POST.getlist("sub")
        Exam = exam(name=exam_name, max_marks=max_marks, ms=True)
        Exam.save()
        for sub_id in sub_ids:
            Subject = subject.objects.get(id=sub_id)
            print(Subject.subject)
            print("save exam done", Exam)
            exam_held_subject = ExamHeldSubject(exam=Exam, subject=Subject)
            exam_held_subject.save()
        # c = request.POST['class']
        # section = request.POST['section']
        # cs = classSection.objects.get(Class = c, section = section)
        # s = request.POST['subject']
        # sub = subject.objects.get(subject = s)
        # name = request.POST['exam']
        # marks = request.POST['marks']
        # date = request.POST['date']
        # test = exam(teacher = t, classSection = cs, subject = sub, date = date, name = name, marks = marks)
        # test.save()
        # return redirect('teacherExamList')
    return render(request, 'createExam.html', {'classes': classes, 'subjects': subjects})


def marksEdit(request, id):
    exam_held = ExamHeldSubject.objects.get(id=id)
    # test = exam_held.exam
    # print(test)
    # test = exam.objects.get(id=id)
    clas = exam_held.subject.Class
    students = student.objects.filter(Class=clas)
    print(students)
    # obj = school.objects.get(school = test.teacher.school.school)
    # students = student.objects.filter(school = obj, Class = test.classSection)
    return render(request, 'marksEdit.html', {'students': students, 'exam_held': exam_held})
    # return render(request, 'marksEdit.html')
    # return HttpResponse(f"This is marksEdit page {id}")

# exam_id-student_id


@api_view(['GET', 'POST'])
def marksUpdate(request):
    if request.method == "GET":
        print(request)
        scores = score.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        # return Response({"msg":"api is being baked"})
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def leaderboard(request, subject_id):
#     studentobj = student.objects.get(user = request.user)
#     classobj = studentobj.Class
#     print(classobj)
#     subjects = subject.objects.filter(Class = classobj)
#     print(subjects)
#     exams = ExamHeldSubject.objects.filter(subject = subject.objects.get(id = subject_id))
#     print("exams:", exams)
#     students = student.objects.filter(Class = classobj)
#     # print(students)
#     marks = []
#     for s in students:
#         m = 0
#         for e in exams:
#             # print(e, s)
#             try:
#                 mark = score.objects.get(exam_held = e, stu = s)
#                 m = m + mark.score
#             except:
#                 m = 0
#         marks.append(m)
#     # print(marks)
#     return render(request, 'leaderboard.html', {'subjects': subjects, 'sub': subjects[0], 'students': students, 'class': classobj, 'marks': marks})

def progress(request, subject_id):
    studentobj = student.objects.get(user = request.user)
    classobj = studentobj.Class
    subjects = subject.objects.filter(Class = classobj)
    subjectobj = subject.objects.get(id = subject_id)
    exams = ExamHeldSubject.objects.filter(subject = subjectobj)
    scores = []
    for e in exams:
        print(e)
        scoreobj = score.objects.get(exam_held = e, stu = studentobj)
        scores.append(scoreobj)
    print(scores)
    return render(request, 'progress.html', {'scores': scores, 'subjects': subjects})


def leaderboard(request):
    print(request.user.id)
    cls = student.objects.get(user = request.user).Class
    print(cls)
    subject_qs = subject.objects.filter(Class = cls)
    print(subject_qs)
    examHeld_qs = ExamHeldSubject.objects.filter(subject__in = subject_qs)
    print(examHeld_qs)
    
    exams_qs = []
    for examHeld_q in examHeld_qs:
        exam_q = exam.objects.get(id = examHeld_q.exam.id)
        exams_qs.append(exam_q)
    print(len(exams_qs))
    exam_qs = set(exams_qs) # remove duplicates
    print(len(exam_qs))    
    return render(request, 'leaderboard.html', {'subjects': subject_qs, 'exams': exam_qs})