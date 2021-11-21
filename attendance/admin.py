from django.contrib import admin
from .models import attendance, Leave
# Register your models here.

@admin.register(attendance)
class attendanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'student', 'present')

@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('student', 'date_from', 'date_to', 'reason')