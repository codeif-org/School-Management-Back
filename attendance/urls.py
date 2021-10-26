from django.urls import path
from . import views

app_name = "attendance"
urlpatterns = [
    path('teacher/', views.Attendance, name='attendance'),
    path('teacher/api/saveAttendance/<int:student_id>', views.saveAttendance, name='saveAttendance'),
    path('student/', views.studentAttendance, name='studentAttendance'),
]