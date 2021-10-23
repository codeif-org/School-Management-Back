from django.contrib import admin
from .models import homework
# Register your models here.
@admin.register(homework)
class homeworkAdmin(admin.ModelAdmin):
    list_display = ('Class', 'topic', 'desc', 'due_date', 'date', 'user')