from django.urls import path
from . import views

app_name = "exam"
urlpatterns = [
    path('superadmin/', views.superadminExam, name='superadminExam'),
    path('superadmin/createexam', views.superadminCreateExam, name='superadminCreateExam'),
    path('teacherExamList/', views.teacherExamList, name='teacherExamList'),
    path('marksEdit/<int:id>', views.marksEdit, name='marksEdit'),
    path('createExam/', views.createExam, name='createExam'),
    path('api/marksupdate/', views.marksUpdate, name='marksUpdate'),
    path('student/leaderboard/', views.leaderboard, name='leaderboard'),
    path('student/leaderboard/api/score', views.scoreAPI, name='scoreAPI'),
    path('student/progress/', views.progress, name='progress'),
    path('api/student/progress', views.progressAPI, name='progressAPI'),
]
