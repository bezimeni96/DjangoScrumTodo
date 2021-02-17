from django.shortcuts import render

from django.contrib.auth.models import User

# Create your views here.
def userInfo(request, pk):
  try:
    user = User.objects.get(pk = pk)
  except User.DoesNotExist:
    return render(request, 'todo/userDoesNotExist.html')

  context = {
    'user': user
  }
  return render(request, 'todo/userInfo.html', context)