from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from todo.api import views

# app_name = 'todo'

urlpatterns = [
  path('home/', views.HomeView.as_view()),
  path('users/<int:pk>/', views.UserViewSet.as_view()),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('login/', views.LoginView.as_view()),
  path('users/me/', views.UserMeView.as_view()),
]

