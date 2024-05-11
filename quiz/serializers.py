from rest_framework import serializers
from .models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        fields = [
            'title',
            'category',
            'question'
        ]