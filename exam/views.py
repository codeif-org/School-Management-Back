from typing import List
from django.shortcuts import render, redirect, HttpResponse
from .models import exam, score, ExamHeldSubject
from superadmin.models import school
from teacher.models import teacher, classSection, subject
from student.models import student
from django.http import JsonResponse
import json

# rest
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from exam.serializers import ScoreSerializer

# Create your views here.
# https://www.dev2qa.com/what-does-double-underscore-__-means-in-django-model-queryset-objects-filter-method/
# field_lookup
# fieldname__lookuptype=value

# for dict sorting
# from collections import OrderedDict
# student_score_dict = OrderedDict(sorted(student_score_dict.items(), key=lambda t: t[1][2], reverse=True))

def superadminExam(request):
    return HttpResponse("This is super admin exam list")

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
    user = request.user
    t = teacher.objects.get(user=user)
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

def progress(request):
    studentobj = student.objects.get(user = request.user)
    classobj = studentobj.Class
    subject_qs = subject.objects.filter(Class = classobj)
    # subjectobj = subject.objects.get(id = subject_id)
    examheld_qs = ExamHeldSubject.objects.filter(subject__in = subject_qs)
    print(examheld_qs)
    scores_dict = {}
    # {"examheld_id": [exam_name, marks, max_marks]}
    for examheld_q in examheld_qs:
        if examheld_q.exam.id not in scores_dict:
            scores_dict[examheld_q.exam.id] = [examheld_q.exam.name, score.objects.get(exam_held=examheld_q, stu=studentobj).score, (examheld_q.exam.max_marks)*len(subject_qs)]
        else:
            scores_dict[examheld_q.exam.id][1] = scores_dict[examheld_q.exam.id][1] + score.objects.get(exam_held=examheld_q, stu=studentobj).score
        print(examheld_q)
        # scoreobj = score.objects.get(exam_held = examheld_q, stu = studentobj)
        # scores.append(scoreobj)
    # print(len(scores))
    print(scores_dict)
    print(len(subject_qs))
    print(scores_dict.keys())
    for item in scores_dict.values():
        percent =  round((item[1]/item[2])*100, 1)
        item.append(percent)
        print(item)
    print(scores_dict)    
    return render(request, 'progress.html', {'scores': scores_dict, 'subjects': subject_qs, 'scores_json': json.dumps(scores_dict)})

def progressAPI(request):
    if "subject" in request.GET:
        subject_id = request.GET["subject"]
        studentobj = student.objects.get(user = request.user)
        examheld_qs = ExamHeldSubject.objects.filter(subject = subject_id)
        # print(examheld_qs)
        scores_qs = score.objects.filter(exam_held__in = examheld_qs, stu = studentobj)
        # print(scores_qs)
        scores_dict = {}
        # exam_id: [exam_name, marks, max_marks, percent]
        for score_q in scores_qs:
            scores_dict[score_q.exam_held.exam.id] = [score_q.exam_held.exam.name, score_q.score, score_q.exam_held.exam.max_marks, round((score_q.score/score_q.exam_held.exam.max_marks)*100, 1)]
        print(scores_dict)
        return JsonResponse(scores_dict, safe=False)
        # return HttpResponse(json.dumps(scores_dict), content_type="application/json")   
        # above both are same 
        # return HttpResponse(scores_qs)
    return HttpResponse(json.dumps({"error": "No subject id"}), content_type="application/json")

def leaderboard(request):
    # print(request.user.id)
    cls = student.objects.get(user = request.user).Class
    # print(cls)
    subject_qs = subject.objects.filter(Class = cls)
    # print(subject_qs)
    examHeld_qs = ExamHeldSubject.objects.filter(subject__in = subject_qs)
    # print(examHeld_qs)
    exams_qs = []
    for examHeld_q in examHeld_qs:
        exam_q = exam.objects.get(id = examHeld_q.exam.id)
        exams_qs.append(exam_q)
    # print(len(exams_qs))
    exam_qs = set(exams_qs) 
    # remove duplicates from exam_qs and exam_qs is a set of exams model objects
    # print(len(exam_qs))    
    return render(request, 'leaderboard.html', {'subjects': subject_qs, 'exams': exam_qs, 'class': cls})


# 127.0.0.1:8000/exam/student/leaderboard/api/score?subject=571&exam=384
def scoreAPI(request):
    print(request.GET)
    if ('subject' in request.GET) and ('exam' in request.GET):
        subject = request.GET['subject']
        exam = request.GET['exam']
        exam_held = ExamHeldSubject.objects.get(subject = subject, exam = exam)
        # print(exam_held)
        score_qs = score.objects.filter(exam_held = exam_held)
        # print(score_qs)
        
        student_score_dict = {} # student_id : [fname, roll_no, score]
        for score_q in score_qs:
            student_obj = student.objects.get(id = score_q.stu.id)
            student_score_dict[score_q.stu.id] = [student_obj.fname, student_obj.roll_no, score_q.score]
        print(student_score_dict) 
        student_score_json = json.dumps(student_score_dict)   
        return HttpResponse(student_score_json)
    
    if 'exam' in request.GET:
        print(request.GET['exam'])
        examHeld_qs = ExamHeldSubject.objects.filter(exam__id = request.GET['exam'])
        # exam__id and exam works same because overall exam is a foreign key in ExamHeldSubject
        # print(examHeld_qs) this gives 5 ExamHeldSubject objects because each subject has 5 exams
        # print(examHeld_qs)
        score_qs = score.objects.filter(exam_held__in = examHeld_qs)
        # print(score_qs)
        # student_ids = []
        score_dict = {} # student_id : score
        for score_q in score_qs:
            # print(score_q.stu.id, score_q.score)
            if score_q.stu.id not in score_dict:
                score_dict[score_q.stu.id] = score_q.score
            else:
                curr_score = score_dict[score_q.stu.id]    
                score_dict[score_q.stu.id] = curr_score + score_q.score
        # print(score_dict)
        # score_json = json.dumps(score_dict)
        # create id list with arguments of student_name, roll number and score
        student_score_dict = {}
        counter=1
        for item in score_dict.items():
            # print(item[0], item[1])
            student_obj = student.objects.get(id = item[0])
            # print(student_obj)
            student_score_dict[counter] = [student_obj.fname, student_obj.roll_no, item[1]]
            counter += 1
        # print(student_score_dict) 
        student_score_json = json.dumps(student_score_dict)   
        return HttpResponse(student_score_json)
    
    if 'subject' in request.GET:
        print(request.GET['subject']) 
        examHeld_qs = ExamHeldSubject.objects.filter(subject__id = request.GET['subject'])    
        print(examHeld_qs) # they're giving the 3 objects because each subject has 3 exams
        score_qs = score.objects.filter(exam_held__in = examHeld_qs)
        # print(score_qs)

        student_score_dict = {} # student_id : [fname, roll_no, score]
        for score_q in score_qs:
            # print(score_q.stu.id, score_q.score)
            student_obj = student.objects.get(id = score_q.stu.id)
            if student_obj not in student_score_dict:
                student_score_dict[student_obj.id] = [student_obj.fname, student_obj.roll_no, score_q.score]
            else:
                curr_score = student_score_dict[student_obj.id][2]
                student_score_dict[student_obj.id] = [student_obj.fname, student_obj.roll_no, curr_score + score_q.score]
        print(student_score_dict)
        student_score_json = json.dumps(student_score_dict)
        return HttpResponse(student_score_json)           
    return HttpResponse("No data found try to do some different parameters")