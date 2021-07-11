from django.urls import path
from carapp import views

#app_name = 'carapp'
urlpatterns = [
    path('', views.cars, name='car'),
    path('<int:id>/', views.car_detail, name='car_detail'),
]
