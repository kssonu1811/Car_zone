from django.shortcuts import render
from . models import Team
from carapp.models import car
# Create your views here.
def home(request):
    teams = Team.objects.all()
    feature_cars = car.objects.filter(is_feature=True).order_by('created_date')
    all_cars = car.objects.order_by('created_date')
    data ={
        'teams' : teams,
        'feature_cars' : feature_cars, 
        'all_cars' : all_cars,
    }
    return render(request, 'phase1/home.html', data,)
def about(request):
    teams = Team.objects.all()
    data ={
        'teams' : teams,
    }
    return render(request, 'phase1/about.html',data,)
def services(request):
    return render(request, 'phase1/service.html')
def contact(request):
    return render(request, 'phase1/contact.html')
def cars(request):
    return render(request, 'phase1/cars.html')
