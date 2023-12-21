from django.contrib import admin 

from .models import CakeOrder, DessertOrder,SpicyOrder,SweetOrder


admin.site.register(CakeOrder)
admin.site.register(DessertOrder)
admin.site.register(SpicyOrder)
admin.site.register(SweetOrder)
