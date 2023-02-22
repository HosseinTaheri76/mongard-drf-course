# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer

# @api_view()
# def home(request):
#     return Response({
#         'NID': '0440687373',
#         'name': "Hossein",
#         'age': 25
#     })

class Home(APIView):
    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(persons, many=True)
        return Response(ser_data.data)


