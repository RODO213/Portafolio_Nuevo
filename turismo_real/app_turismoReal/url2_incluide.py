
from app_turismoReal import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    # url('',views.vista2, name="vista2"),
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('index/', views.home, name='home-index'),
    path('login/', views.login, name='home-login'),
    path('registro/', views.registro, name='home-registro'),

   
    
]
