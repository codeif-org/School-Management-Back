from django.urls import path
from . import views

app_name = "student"
urlpatterns = [
    path('home/', views.studenthome, name='studenthome'),
    path('notice/', views.notice, name='notice'),
    path('progress/', views.progress, name='progress'),
]
