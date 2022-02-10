from django.urls import path
from . import views
from notice import views as notice_views

app_name = "superadmin"
urlpatterns = [
    path('home/', views.adminhome, name = 'adminhome'),
    path('addTeacher/', views.addTeacher, name = 'addTeacher'),
    path('addStudent/', views.addStudent, name = 'addStudent'),
    path('students/', views.students, name = 'students'),
    path('teachers/', views.teachers, name = 'teachers'),
    # path('notice/', notice_views.showNotice, name = 'notice'),
    path('info/', views.info, name = 'info'),
    path('api/schoolinfo/', views.infoAPI, name = 'infoAPI'),
    path('classes/', views.classes, name='classes'),
]
