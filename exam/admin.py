from django.contrib import admin
from .models import exam, score, ExamHeldSubject
# Register your models here.

@admin.register(exam)
class examAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'max_marks', 'date',)

@admin.register(score)
class scoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_held','stu', 'score')

@admin.register(ExamHeldSubject)
class ExamHeldSubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam', 'subject')    