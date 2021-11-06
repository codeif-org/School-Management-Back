from django.contrib import admin
from .models import school, SuperAdmin
# Register your models here.

@admin.register(school)
class schoolAdmin(admin.ModelAdmin):
    list_display = ('school', 'address', 'city', 'pin', 'state', 'country', 'regno')
@admin.register(SuperAdmin)
class superAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'school')