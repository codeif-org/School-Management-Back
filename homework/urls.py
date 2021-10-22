from django.urls import path
from . import views

app_name = "homework"
urlpatterns = [
    path('teacher/', views.homeworkTeacher, name='homeworkTeacher'),
    path('teacher/createHomework/', views.createHomework, name='createHomework'),
]
