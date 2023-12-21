
from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    
    path('', views.beauty, name="beauty"),
    path('ordercart/', views.ordercart, name="ordercart"),
    path('finalchck/', views.finalchck, name="finalchck"),
    path('finalchck/calculator', views.calculator, name="calculator"),

    
    

]
