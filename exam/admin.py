from django.contrib import admin
from .models import exam, score
# Register your models here.

@admin.register(exam)
class examAdmin(admin.ModelAdmin):
    list_display = ('classSection', 'subject', 'date', 'name', 'max_marks')

@admin.register(score)
class scoreAdmin(admin.ModelAdmin):
    list_display = ('exam', 'score')