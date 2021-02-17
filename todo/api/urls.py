from django.urls import path


from todo.api import views

app_name = 'todo'

urlpatterns = [
  path('home/', views.HomeView.as_view()),
]