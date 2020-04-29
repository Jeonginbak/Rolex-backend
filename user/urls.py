from django.urls import path

from .views import SignUp, LogIn, LikeView, MyLikeListPreview, MyLikeListDetail


urlpatterns = [
	path('/login', LogIn.as_view()),
    path('/sign-up', SignUp.as_view()),
	path('/like', LikeView.as_view()),
	path('/mylike/preview', MyLikeListPreview.as_view()),
	path('/mylike/detail', MyLikeListDetail.as_view()),
]
