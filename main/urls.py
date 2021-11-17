
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('explore/', views.explore_view, name='explore_view'),
]
