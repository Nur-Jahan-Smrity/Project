
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns =[
    
    path('', views.foodpage,name="foodpage"),
    path('Cakes', views.Cakes,name="Cakes"),
    path('Dessert', views.Dessert,name="Dessert"),
    path('SpicyFood', views.SpicyFood,name="SpicyFood"),
    path('Sweets', views.Sweets,name="Sweets"),
    path('Cake_Order/', views.Cake_Order,name="Cake_Order"),
    path('Dessert_Order/', views.Dessert_Order,name="Dessert_Order"),
    path('Spicy_Food/', views.Spicy_Order,name="Spicy_Order"),
    
    path('Sweet_order/', views.Sweet_order,name="Sweet_order"),

    path('Calculatec/', views.Calculatec,name="Calculatec"),
    path('Calculated/', views.Calculated,name="Calculated"),
    path('Calculates/', views.Calculates,name="Calculates"),
    path('Calculatess/', views.Calculatess,name="Calculatess"),
    
    
]