from django.shortcuts import render, get_object_or_404

from DiegoPerezPortfolio.models import Project


# Create your views here.


def index(request):
    return render(request, 'index.html')

def project(request, project_name):
    curr_project = get_object_or_404(Project, title=project_name)
    return render(request, 'project.html', context={'project': curr_project})