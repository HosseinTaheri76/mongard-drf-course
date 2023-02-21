# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

# @api_view()
# def home(request):
#     return Response({
#         'NID': '0440687373',
#         'name': "Hossein",
#         'age': 25
#     })

class Home(APIView):
    def get(self, request):
        return Response({
            'NID': '0440687373',
            'name': "Hossein",
            'age': 25
        })
