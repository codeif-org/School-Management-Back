from django.urls import path
from . import views

app_name = "homework"
urlpatterns = [
    path('teacher/', views.homeworkTeacher, name='homeworkTeacher'),
    path('teacher/createHomework/', views.createHomework, name='createHomework'),
    path('teacher/api/createHomework/', views.homeworkAPI, name='homeworkAPI'),
    path('student/', views.homeworkStudent, name='homework'),
]
