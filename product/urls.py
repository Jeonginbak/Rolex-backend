from django.urls import path

from .views import DetailView, ConfigView, ListView

urlpatterns = [
    path('/<int:product_id>', DetailView.as_view()),
    path('/config/<str:option>', ConfigView.as_view()),
    path('/list', ListView.as_view()),
]
