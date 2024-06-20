from rest_framework import serializers
from .models import api

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=api
        fields=['id', 'type', 'difficulty', 'category', 'question', 'correct_answer', 'incorrect_answers']