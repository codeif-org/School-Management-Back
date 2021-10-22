from django.contrib import admin
from .models import exam, score
# Register your models here.

@admin.register(exam)
class examAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'classSection', 'subject', 'date', 'name', 'marks')

@admin.register(score)
class scoreAdmin(admin.ModelAdmin):
    list_display = ('exam', 'score')