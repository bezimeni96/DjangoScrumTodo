from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns



from todo.api import views

# app_name = 'todo'

urlpatterns = [
  path('home/', views.HomeView.as_view()),
  path('users/<int:pk>/', views.UserViewSet.as_view()),
]