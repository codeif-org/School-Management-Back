from django.shortcuts import render, HttpResponse
from superadmin.models import school
from student.models import student
from teacher.models import classSection, subject
# Create your views here.
import json

def studenthome(request):
    studentobj = student.objects.get(user = request.user)
    schoolobj = studentobj.school
    sub = subject.objects.filter(Class = studentobj.Class)
    return render(request, 'index.html', {'student': studentobj, 'sub': sub[0], 'school': schoolobj})

# http://127.0.0.1:8000/student/api/classStudent?class=21
# this can also be implented using Rest API in Django
def classStudentAPI(request):
    if "class" in request.GET:
        class_id = request.GET['class']
        student_qs = student.objects.filter(Class = class_id)
        # print(student_qs)
        student_dict = {}
        for student_q in student_qs:
            student_dict[student_q.id] = student_q.fname
        if len(student_dict) == 0:
            return HttpResponse(json.dumps({"error": "No student found"}), content_type="application/json")
        else:    
            return HttpResponse(json.dumps(student_dict), content_type='application/json')
    return HttpResponse(json.dumps({"msg": "Please pass class id in params"}), content_type='application/json')