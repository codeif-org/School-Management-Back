from django.contrib import admin
from .models import Homework, Student_Homework
# Register your models here.
@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('topic', 'desc', 'due_date', 'date')

@admin.register(Student_Homework)
class Student_HomeworkAdmin(admin.ModelAdmin):
    list_display = ('homework', 'Class')