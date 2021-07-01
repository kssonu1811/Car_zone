from django.db.models.base import Model
from django.http import request
from django.shortcuts import render
from . models import Team
from carapp.models import car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def home(request):
    teams = Team.objects.all()
    feature_cars = car.objects.filter(is_feature=True).order_by('created_date')
    all_cars = car.objects.order_by('created_date')
    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct()
    data ={
        'teams' : teams,
        'feature_cars' : feature_cars, 
        'all_cars' : all_cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
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
    cars = car.objects.order_by('created_date')
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct()
    data ={
        'cars' : paged_cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
    }
    return render(request, 'phase1/cars.html', data,)
def search(request):
    cars = car.objects.order_by('created_date')
    model_search = car.objects.values_list('model', flat=True).distinct()
    city_search = car.objects.values_list('city', flat=True).distinct()
    year_search = car.objects.values_list('year', flat=True).distinct()
    body_style_search = car.objects.values_list('body_style', flat=True).distinct()
    condition_search = car.objects.values_list('condition', flat=True).distinct()
    transmission_search = car.objects.values_list('transmission', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(car_title__icontains=keyword)
    
    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)
    
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    
    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)
   
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data ={
        'cars' : cars,
        'model_search' : model_search,
        'city_search' : city_search,
        'year_search' : year_search,
        'body_style_search' : body_style_search,
        'condition_search' : condition_search,
        'transmission_search' : transmission_search,
    }
    return render(request, 'cars/search.html', data,)
 