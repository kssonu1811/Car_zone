from django.urls import path
from carapp import views

urlpatterns = [
    path('', views.cars, name='car'),
]
