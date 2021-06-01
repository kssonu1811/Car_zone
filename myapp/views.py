from django.shortcuts import render
from . models import Team
# Create your views here.
def home(request):
    teams = Team.objects.all()
    data ={
        'teams' : teams,
    }
    return render(request, 'phase1/home.html', data)
def about(request):
    teams = Team.objects.all()
    data ={
        'teams' : teams,
    }
    return render(request, 'phase1/about.html',data)
def services(request):
    return render(request, 'phase1/service.html')
def contact(request):
    return render(request, 'phase1/contact.html')
def cars(request):
    return render(request, 'phase1/cars.html')
