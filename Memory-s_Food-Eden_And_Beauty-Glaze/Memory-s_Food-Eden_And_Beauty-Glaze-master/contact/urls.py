
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns =[
    path('admin/', admin.site.urls),

    path('', views.contactus,name="contactus"),
    path('Contact_us', views.contactus,name="contactus"),
    path('Contact/',views.Contact,name="Contact"),
   # path('Contact_us/Contact_us',views.contactus,name="contactus"),
    
]