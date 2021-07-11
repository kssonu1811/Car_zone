from django.urls import path
from account import views


my_app = "account"
urlpatterns = [
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
]