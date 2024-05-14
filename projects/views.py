from django.shortcuts import render
from projects.models import *


def project_index(request):
    projects = Project.objects.all()
    images = (Image.objects.filter(project = x).first() for x in projects)
    p_i_zip = zip(list(projects),images)
    context = {
        "projects": p_i_zip
    }
    return render(request, "project_index.html", context)

