from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'phase1/home.html')
def about(request):
    return render(request, 'phase1/about.html')
def services(request):
    return render(request, 'phase1/service.html')
def contact(request):
    return render(request, 'phase1/contact.html')
def cars(request):
    return render(request, 'phase1/cars.html')
