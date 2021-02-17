from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from todo.models import ToDo


class HomeView(APIView):
  def get(self, request):
    all_todos = ToDo.objects.all().values()
    current_user = request.user
    return Response({
      "Loged user" : current_user.username,
      "Message" : "List of all todos",
      "Todo list" : all_todos})