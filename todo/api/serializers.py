from rest_framework import serializers


from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
  username = serializers.CharField(max_length = 128)
  password = serializers.CharField(max_length = 128, write_only = True)
  email = serializers.EmailField(max_length = 128, read_only = True)

  class Meta:
    model = User
    fields = ['pk', 'username', 'password', 'email']