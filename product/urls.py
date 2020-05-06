from django.urls import path

from .views import DetailView, ConfigSizeView, ConfigMaterialView
from .views import ConfigBezelView, ConfigBraceletView, ConfigDialView
from .views import ListView

urlpatterns = [
    path('/list', ListView.as_view()),
    path('/<int:product_id>', DetailView.as_view()),
    path('/config/model', ConfigSizeView.as_view()),
    path('/config/material', ConfigMaterialView.as_view()),
    path('/config/bezel', ConfigBezelView.as_view()),
    path('/config/bracelet', ConfigBraceletView.as_view()),
    path('/config/dial', ConfigDialView.as_view()),
]
