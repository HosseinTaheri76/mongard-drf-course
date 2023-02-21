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
        print(request.data)
        return Response({
            'NID': '0440687373',
            'name': request.query_params.get('name', 'not specified'),
            'age': 25
        })

    def post(self, request):
        data = request.data
        return Response({v: k for k, v in data.items()})
