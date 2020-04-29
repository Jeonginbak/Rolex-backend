from django.urls import path

from .views import SignUp, LogIn, LikeView


urlpatterns = [
	path('/login', LogIn.as_view()),
    path('/sign-up', SignUp.as_view()),
	path('/like', LikeView.as_view()),
]
