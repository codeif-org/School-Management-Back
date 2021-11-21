from django.urls import path
from . import views

app_name = "homework"
urlpatterns = [
    path('teacher/', views.homeworkTeacher, name='homeworkTeacher'),
    path('teacher/createHomework/', views.createHomework, name='createHomework'),
    path('teacher/homeworkList/<int:homework_id>', views.homeworkList, name='homeworkList'),
    # path('teacher/api/createHomework/', views.homeworkAPI, name='homeworkAPI'),
    path('student/<int:id>', views.homeworkStudent, name='homework'),
    path('student/submitHomework/<int:homework_id>', views.submitHomework, name='submitHomework'),
]