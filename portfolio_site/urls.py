# File created 5/3/2024 by Athin Shetty
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pages.urls"))
]
