from django.urls import path
from . import views

app_name = "attendance"
urlpatterns = [
    path('teacher/', views.Attendance, name='attendance'),
    path('teacher/api/saveAttendance/', views.saveAttendance, name='saveAttendance'),
    path('student/', views.studentAttendance, name='studentAttendance'),
    path('student/applyLeave', views.applyLeave, name='applyLeave'),
]