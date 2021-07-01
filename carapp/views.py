from carapp.models import car
from django.shortcuts import get_object_or_404, render

# Create your views here.
def cars(request):
    cars = car.objects.order_by('created_date')
    data ={
        'cars' : cars,
    }
    return render(request, 'cars/car.html', data,)
def car_detail(request, id):
    single_car = get_object_or_404(car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data,)
