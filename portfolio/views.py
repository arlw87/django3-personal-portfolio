from django.shortcuts import render
from .models import PortfolioProject
from tech.models import Technologies

# Create your views here.
def home (request):

    #grab project objects from the database
    #grabs all the objects from the database
    projects = PortfolioProject.objects.all()
    technologies = Technologies.objects.all()
    print(projects)
    return render(request, 'portfolio/home.html', {'projects' : projects, 'technologies' : technologies})
