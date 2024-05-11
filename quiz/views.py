# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Question
from .serializers import QuizSerializer
from rest_framework.views import APIView

class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()