from rest_framework import serializers
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken


from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
  username = serializers.CharField(max_length = 128)
  password = serializers.CharField(max_length = 128, write_only = True)
  email = serializers.EmailField(max_length = 128, read_only = True)
  first_name = serializers.CharField(max_length = 128, read_only = True)
  last_name = serializers.CharField(max_length = 128, read_only = True)


  class Meta:
    model = User
    fields = ['pk', 'username', 'password', 'email', 'first_name', 'last_name']


class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=68)
  password = serializers.CharField(max_length=68, min_length=6, write_only=True)
  token_access = serializers.CharField(max_length=512, read_only=True)
  token_refresh = serializers.CharField(max_length=512, read_only=True)
  email = serializers.EmailField(max_length=68, min_length=6, read_only=True)

  class Meta:
    model = User
    fields = ['email', 'username', 'password', 'token_refresh', 'token_access']

  def validate(self, attrs):
    username = attrs.get('username', '')
    password = attrs.get('password', '')

    user = auth.authenticate(username = username, password=password)

    if not user:
      raise AuthenticationFailed('invalid credentials')

    refresh = RefreshToken.for_user(user)

    return {
      'email': user.email,
      'username':user.username,
      'first_name':user.first_name,
      'last_name':user.last_name,
      'token_refresh': str(refresh),
      'token_access':str(refresh.access_token)
    }