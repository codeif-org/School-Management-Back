from rest_framework import serializers
from .models import attendance

class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendance
        fields = ('present', 'student', 'date')