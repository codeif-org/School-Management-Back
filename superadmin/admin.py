from django.contrib import admin
from .models import school
# Register your models here.

@admin.register(school)
class schoolAdmin(admin.ModelAdmin):
    list_display = ('school', 'address', 'city', 'pin', 'state', 'country', 'regno')