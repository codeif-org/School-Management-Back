from django.urls import path
from . import views

app_name = "exam"
urlpatterns = [
    path('teacherExamList/', views.teacherExamList, name='teacherExamList'),
    path('marksEdit/<int:id>', views.marksEdit, name='marksEdit'),
    path('createExam/', views.createExam, name='createExam'),
    path('api/marksupdate/', views.marksUpdate, name='marksUpdate'),
    path('student/leaderboard/<int:subject_id>', views.leaderboard, name='leaderboard'),
    path('student/progress/<int:subject_id>', views.progress, name='progress'),
]
