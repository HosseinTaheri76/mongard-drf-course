from rest_framework import serializers
from django.core.validators import MinLengthValidator

from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'validators': [MinLengthValidator(3, 'username must be at least 3 characters.')]}
        }

    def validate_username(self, value):
        if 'admin' in value:
            raise serializers.ValidationError('using admin as username is prohibited.')
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('password confirm mismatch.')
        return attrs
