from django.contrib import admin
from .models import attendance
# Register your models here.

@admin.register(attendance)
class attendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'student', 'present')