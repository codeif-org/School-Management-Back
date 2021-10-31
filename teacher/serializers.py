from rest_framework import serializers
from teacher.models import subject

class SubjectSerializer(models.ModelSerializer):
    class Meta:
        model = subject
        fields = "__all__"