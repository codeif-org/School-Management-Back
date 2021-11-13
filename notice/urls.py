from django.urls import path
from . import views

app_name = "notice"
urlpatterns = [
    path('teacher/<str:category>', views.teacherNotice, name='teacherNotice'),
    path('createNotice/', views.createNotice, name='createNotice'),
    path('student/notice/', views.studentNotice, name='studentNotice'),
    path('superadmin/<str:category>', views.superAdminNotice, name = 'superAdminNotice'),   
]
