from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('', index, name='index'),
    path('portfolio-details/', portfoliodetails, name='portfoliodetails'),
    path('service-details/', servicedetails, name='servicedetails'),
    path('starter-page/', starterpage, name='starterpage'),
]
