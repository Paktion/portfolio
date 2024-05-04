# File created 5/3/2024 by Athin Shetty
from django.shortcuts import render

# Created 5/3/2024 by Athin Shetty: View for index of site
def home(request):
    return render(request, "pages/home.html", {})