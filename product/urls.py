from django.urls import path

from .views import DetailView, ConfigView

urlpatterns = [
        path('/<int:product_id>', DetailView.as_view()),
        path('/config/<str:option>', ConfigView.as_view()),
        ]
