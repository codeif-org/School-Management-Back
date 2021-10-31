from django.urls import path
from . import views

app_name = "superadmin"
urlpatterns = [
    path('home/', views.adminhome, name = 'adminhome'),
    path('addTeacher/', views.addTeacher, name = 'addTeacher'),
    path('addStudent/', views.addStudent, name = 'addStudent'),
]
