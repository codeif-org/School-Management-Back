from django.shortcuts import render, redirect, HttpResponse
from .models import exam, score
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

# sub: [subject ids array]
def createExam(request):
    obj = request.user
    t = teacher.objects.get(username = obj.username)
    subjects = subject.objects.filter(teacher = t)
    classes = classSection.objects.filter(teacher = t)
    if request.method == "POST":
        print(request.POST)
        print("subjects selected:", request.POST.getlist('sub'))
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
    test = exam.objects.get(id = id)
    clas = test.classSection
    students = student.objects.filter(Class=clas)
    print(students) 
    # obj = school.objects.get(school = test.teacher.school.school)
    # students = student.objects.filter(school = obj, Class = test.classSection)
    return render(request, 'marksEdit.html', {'students': students, 'exam': test})
    # return render(request, 'marksEditTest.html')
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