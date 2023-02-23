from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import MinLengthValidator

from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[
        UniqueValidator(queryset=User.objects.all()),
        MinLengthValidator(3, 'username must be at least 3 characters.')
    ])
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('password confirm mismatch.')
        return attrs
