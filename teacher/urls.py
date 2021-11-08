from django.urls import path
from . import views

app_name = "teacher"
urlpatterns = [
    path('home/', views.teacherhome, name = 'teacherhome'),
    path('addStudent/<int:class_name>', views.addStudent, name = 'addStudent'),
    path('yourClasses/', views.YourClasses, name = 'yourClasses'),
    path('classStudentList/<int:class_id>', views.classStudentList, name = 'classStudentList'),
    path('addStudents/', views.addStudents, name='addStudents'),
    path('api/subject/', views.subjectAPI, name='subjectAPI'),
]
