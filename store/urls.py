from django.urls import path
from .views import Login, Home, Signup

urlpatterns = [
    path('', Home.as_view()),
    path('signup', Signup.as_view()),
    path('login', Login.as_view()),
]
