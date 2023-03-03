from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics

from .serializers import UserRegisterSerializer, UserSerializer


class UserRegister(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializer(data=request.data)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = User.objects.all()

    def list(self, request):
        srz_data = UserSerializer(self.queryset, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        srz_data = UserSerializer(
            generics.get_object_or_404(self.queryset, pk=pk)
        ).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        srz_data = UserSerializer(
            generics.get_object_or_404(self.queryset, pk=pk),
            data=request.data,
            partial=True
        )
        srz_data.is_valid(raise_exception=True)
        srz_data.save()
        return Response(srz_data.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        self.queryset.filter(id=pk).update(is_active=False)
        return Response({'info': 'user deleted'}, status=status.HTTP_204_NO_CONTENT)
