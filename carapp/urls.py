from django.urls import path
from carapp import views

urlpatterns = [
    path('', views.cars, name='car'),
    path('<int:id>/', views.car_detail, name='car_detail'),
]
