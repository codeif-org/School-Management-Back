from django.contrib import admin
from .models import notice
# Register your models here.
@admin.register(notice)
class noticeAdmin(admin.ModelAdmin):
    list_display = ('user', 'classes', 'students', 'topic', 'desc', 'date')