from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .mixins import RetrieveModelMixin

from todo.models import ToDo
from django.contrib.auth.models import User
from todo.api.serializers import UserSerializer, LoginSerializer


class HomeView(APIView):
  def get(self, request):
    all_todos = ToDo.objects.all().values()
    current_user = request.user
    return Response({
      "Loged user" : current_user.username,
      "Message" : "List of all todos",
      "Todo list" : all_todos})



class UserViewSet(RetrieveModelMixin, APIView):

  def get(self, request, pk):
    try:
      user = User.objects.get(pk = pk)
    except User.DoesNotExist:
      return Response({"Message" : "User dosent exist."}, status = status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)



class LoginView(APIView):
  serializer_class = LoginSerializer

  def post(self,request):
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(serializer.data, status=status.HTTP_200_OK)



class UserMeView(APIView):

  def get(self, request):
    current_user = self.request.user
    return Response({
      "pk" : current_user.pk,
      "Username" : current_user.username,
      "Email" : current_user.email,
      "First name" : current_user.first_name,
      "Last name" : current_user.last_name,
      })



class FilterUserView(APIView):
  def get(self, request):

    searchTerm = request.data['name']
    all_users = User.objects.all().filter(first_name__contains = searchTerm).values() | User.objects.all().filter(last_name__contains = searchTerm).values()
    if (len(all_users) < 1):
      return Response({"Message" : "There is not user with this search term."}, status = status.HTTP_404_NOT_FOUND)

    fitered_users = []
    for person in all_users:
      serializer = UserSerializer(person)
      fitered_users.append(serializer.data)

    return Response({
      "Search term": searchTerm,
      "Filtered users": fitered_users,
    })