from django.contrib import admin
from .models import student
# Register your models here.

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('fname', 'mname', 'lname', 'dob', 'email', 'phone', 'fathername', 'mothername', 'fatheremail', 'fatherphone', 'address', 'roll_no', 'Class')