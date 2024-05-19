from django.urls import path
from . import views

urlpatterns =[
    path('', views.home),
    path('first/', views.first_page),
    path('first/second/', views.second_page),
    
]