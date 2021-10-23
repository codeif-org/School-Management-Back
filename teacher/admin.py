from django.contrib import admin
from .models import teacher, classSection, subject

# Register your models here.
# @admin.register(teacher)
# class teachersAdmin(admin.ModelAdmin):
#     list_display = ['fname', 'mname', 'lname', 'email', 'phone']
admin.site.register(teacher)

@admin.register(classSection)
class classSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'Class', 'section', 'teacher')

@admin.register(subject)
class subjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'Class', 'teacher')
