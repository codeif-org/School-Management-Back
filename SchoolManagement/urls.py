"""SchoolManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from teacher import views
import logapp
from logapp import views
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from .settings import LOGOUT_REDIRECT_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.login, name='login'),
    path('logout/', LogoutView.as_view(next_page=LOGOUT_REDIRECT_URL), name='logout'),
    path('teacher/', include('teacher.urls')),
    path('attendance/', include('attendance.urls')),
    path('student/', include('student.urls')),
    path('exam/', include('exam.urls')),
    path('homework/', include('homework.urls')),
    path('notice/', include('notice.urls')),
    path('superadmin/', include('superadmin.urls')),
]
