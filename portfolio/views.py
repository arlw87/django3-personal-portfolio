from django.shortcuts import render
from .models import PortfolioProject

# Create your views here.
def home (request):

    #grab project objects from the database
    #grabs all the objects from the database
    projects = PortfolioProject.objects.all()
    print(projects)
    return render(request, 'portfolio/home.html', {'projects' : projects})
