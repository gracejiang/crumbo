
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('explore/', views.explore_view, name='explore_view'),
    path('grac/', views.grac_view, name='grac_view'),
    path('cxlu/', views.cxlu_view, name='cxlu_view'),
    path('foodplace/<str:id>/', views.foodplace_view, name='foodplace_view'),
]