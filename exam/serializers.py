from rest_framework import serializers
from exam.models import score

# Create your exam api serializers here
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = score
        fields = "__all__"