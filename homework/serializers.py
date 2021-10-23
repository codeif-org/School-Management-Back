from rest_framework import serializers
from .models import homework

class homeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = homework
        fields = ('Class', 'topic', 'desc', 'due_date', 'user')