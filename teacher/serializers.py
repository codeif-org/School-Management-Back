from rest_framework import serializers
from teacher.models import subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = "__all__"