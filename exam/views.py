from typing import List
from django.shortcuts import render, redirect, HttpResponse
from .models import exam, score, ExamHeldSubject
from superadmin.models import school, SuperAdmin
from teacher.models import teacher, classSection, subject
from student.models import student
from django.http import JsonResponse
import json

# rest
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
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
    superadminobj = SuperAdmin.objects.get(user = request.user)
    # print(superadminobj)
    schoolobj = superadminobj.school
    # print(schoolobj)
    teacher_qs = teacher.objects.filter(school = schoolobj)
    # print(len(teacher_qs))
    class_qs = classSection.objects.filter(teacher__in = teacher_qs).values().order_by('Class')
    # print(class_qs)
    subject_qs = subject.objects.filter(teacher__in = teacher_qs)
    # print(len(subject_qs))
    examheld_qs = ExamHeldSubject.objects.filter(subject__in = subject_qs)
    print(len(examheld_qs))
    
    return render(request, 'superadminExam.html', {"exam_lst": examheld_qs, "classes": class_qs})

# here after selecting the class we have two options to embed the subject data
# 1. by sending from django to javascript
# 2. by calling api from javascript
def superadminCreateExam(request):
    user = request.user
    # t = teacher.objects.get(user=user)
    schoolobj = SuperAdmin.objects.get(user = user).school
    # print(schoolobj)
    # this will gives all the teachers of the school
    teacher_qs = teacher.objects.filter(school = schoolobj)
    # this will gives the unique classes of the school
    # class_qs = classSection.objects.filter(teacher__in = teacher_qs).values_list('Class', flat=True).distinct()
    class_qs = classSection.objects.filter(teacher__in = teacher_qs).values().order_by('Class')
    # print(class_qs)
    # print(class_qs.order_by('Class'))
    # print(sorted(class_qs.items(), key = lambda kv:(kv[1], kv[0]))) 
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
        return redirect('exam:superadminExam')
    return render(request, 'superadminCreateExam.html', {'classes': class_qs})

def teacherExamList(request):
    usr = request.user
    teacherobj = teacher.objects.get(user=usr)
    # queryset for subject teachers
    subject_qs = subject.objects.filter(teacher=teacherobj)
    # class_qs = subject_qs.values_list('Class', flat=True).distinct()
    # class_qs = subject.objects.select_related('Class').all().distinct()
    class_qs = []
    for subject_q in subject_qs:
        if subject_q.Class not in class_qs:
            class_qs.append(subject_q.Class)
    # print(subject_qs)
    # __in use for multiple objects or queryset to filter another queryset
    # exam_qs = []
    exam_qs = ExamHeldSubject.objects.filter(subject__in = subject_qs)
    # print(exam_qs)
    
    # queryset exam_qs_1 for class teachers
    try:
        class_qs_1 = classSection.objects.get(teacher=teacherobj)
    except:
        class_qs_1 = None
    subject_qs_1  = subject.objects.filter(Class=class_qs_1)
    # print(subject_qs_1)
    exam_qs_1 = ExamHeldSubject.objects.filter(subject__in = subject_qs_1)
    # print(exam_qs_1)
    
    # union of both the queryset
    exam_qs = exam_qs.union(exam_qs_1)
    class_qs.append(class_qs_1)
    # print(class_qs)
    class_qs = set(class_qs)
    print("class_qs ", class_qs)
    return render(request, 'teacherExamList.html', {'exam_lst': exam_qs, 'classes': class_qs})


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
    return render(request, 'createExam.html', {'classes': classes, 'subjects': subjects, 'school': school})

def superadminMarksEdit(request, id):
    user = request.user
    exam_held = ExamHeldSubject.objects.get(id=id)
    class_q = exam_held.subject.Class
    superadmin=SuperAdmin.objects.filter(user=user)
    if superadmin:
        print("auth")    
        student_qs = student.objects.filter(Class=class_q).values()
        for student_q in student_qs:
            if score.objects.filter(stu=student_q['id'], exam_held=id).exists():
                student_q['score'] = score.objects.get(stu=student_q['id'], exam_held=id).score
            else:
                student_q['score'] = "--"
        return render(request, 'superadminMarksEdit.html', {'students': student_qs, 'exam_held': exam_held})

def teacherMarksEdit(request, id):
    user = request.user
    exam_held = ExamHeldSubject.objects.get(id=id)
    class_q = exam_held.subject.Class
    subject_q = exam_held.subject
    teacherobj = teacher.objects.get(user=user) # verify that user is teacher
    class_teacher_verify = classSection.objects.get(teacher=teacherobj) # verify that user is teacher of class
    print("class_teacher_verify_qs ", class_teacher_verify)
    subject_teacher_verify = subject.objects.filter(teacher=teacherobj) # verify that user is teacher of subjects      
    
    # if user is teacher and ((is teacher of class) or (is teacher of subject)) then only he/she can edit
    if class_q == class_teacher_verify or subject_q in subject_teacher_verify:
        student_qs = student.objects.filter(Class=class_q).values()
        for student_q in student_qs:
            if score.objects.filter(stu=student_q['id'], exam_held=id).exists():
                student_q['score'] = score.objects.get(stu=student_q['id'], exam_held=id).score
            else:
                student_q['score'] = "--"
        return render(request, 'teacherMarksEdit.html', {'students': student_qs, 'exam_held': exam_held})



@api_view(['GET', 'POST'])
def marksUpdate(request):
    def check_score(request):
        print("check_score")
        print(request.data)
        if score.objects.filter(stu=request.data['stu'], exam_held=request.data['exam_held']).exists():
            request_method = "PUT"
        else:
            request_method = "POST"    
        print(request_method)
        return request_method
    request_method = check_score(request) 
       
    if request.method == "GET":
        print(request)
        scores = score.objects.all()
        serializer = ScoreSerializer(scores, many=True)
        # return Response({"msg":"api is being baked"})
        return Response(serializer.data)
    if request_method == "POST":
        print(type(request.method))
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Marks Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request_method == "PUT":
        print(type(request.method))
        score_qs = score.objects.get(stu=request.data['stu'], exam_held=request.data['exam_held'])
        serializer = ScoreSerializer(score_qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Marks Updated Successfully"}, status=status.HTTP_202_ACCEPTED)    
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
    # student_id : [fname, roll_no, score]
    class_student_qs = student.objects.filter(Class = cls)
    score_qs = score.objects.filter(stu__in = class_student_qs)
    student_scores_dict = {}
    for score_q in score_qs:
        if score_q.stu.id not in student_scores_dict:
            student_scores_dict[score_q.stu.id] = [score_q.stu.fname, score_q.stu.roll_no, score_q.score]
        else:
            student_scores_dict[score_q.stu.id][2] = student_scores_dict[score_q.stu.id][2] + score_q.score
    student_scores_dict_sorted = list(sorted(student_scores_dict.items(), key=lambda x: x[1][2], reverse=True))    
    print(student_scores_dict_sorted)   
    # print(student_score_sort)     
    return render(request, 'leaderboard.html', {'subjects': subject_qs, 'exams': exam_qs, 'class': cls, 'scores_dict': student_scores_dict_sorted})


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
