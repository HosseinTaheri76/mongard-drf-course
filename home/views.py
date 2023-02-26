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

    def post(self, request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message': 'question deleted'}, status=status.HTTP_200_OK)
