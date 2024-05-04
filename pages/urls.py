# File created 5/3/2024 by Athin Shetty
from django.urls import path
from pages import views

urlpatterns = [
    path("", views.home, name='home'),
]