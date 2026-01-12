from django.urls import path
from online_store import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
]