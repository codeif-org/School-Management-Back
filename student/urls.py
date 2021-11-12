from django.urls import path
from . import views

app_name = "student"
urlpatterns = [
    path('home/', views.studenthome, name='studenthome'),
    path('api/classStudent', views.classStudentAPI, name = 'classStudentAPI'),
]
