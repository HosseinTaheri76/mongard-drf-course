from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from .models import Person, Question, Answer
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer


class Home(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(persons, many=True)
        return Response(ser_data.data)

class QuestionView(APIView):

    def get(self, request):
        srz_data = QuestionSerializer(Question.objects.all(), many=True).data
        return Response(srz_data)
