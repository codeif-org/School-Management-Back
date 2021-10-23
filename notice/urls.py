from django.urls import path
from . import views

app_name = "notice"
urlpatterns = [
    path('teacher/showNotice/', views.showNotice, name='showNotice'),
    path('teacher/createNotice/', views.createNotice, name='createNotice'),
    path('student/notice/', views.studentNotice, name='studentNotice'),
]
