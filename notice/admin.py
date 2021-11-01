from django.contrib import admin
from .models import notice, receiver
# Register your models here.
# @admin.register(notice)
# class noticeAdmin(admin.ModelAdmin):
#     list_display = ('topic', 'desc', 'date')
admin.site.register(notice)

@admin.register(receiver)
class receiverAdmin(admin.ModelAdmin):
    list_display = ('note', 'receiver', 'posted_by')