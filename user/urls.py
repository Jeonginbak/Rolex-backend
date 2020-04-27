from django.urls import path

from .views import SignUp, LogIn


urlpatterns = [
    path('/login', LogIn.as_view()),
    path('/sign-up', SignUp.as_view()),
]
