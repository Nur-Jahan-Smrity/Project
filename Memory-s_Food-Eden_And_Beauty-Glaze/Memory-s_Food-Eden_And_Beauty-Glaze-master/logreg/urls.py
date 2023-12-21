
from django.contrib import admin
from django.urls import path,include
from Registration import views
from Registration.views import RegisterView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('registerform/', views.registerform, name="registerform"),
    path('loginform/', views.loginform, name="loginform"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='blog/index.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name="logout"),

    path('Contact_us/', include('contact.urls') ),
    path('home/Contact_us/', include('contact.urls') ),

    path('Contact/', include('contact.urls') ),
    path('home/Contact/', include('contact.urls') ),

    path('About/', include('about.urls') ),
    path('home/About/', include('about.urls')),

    path('Feedback/',include('feedback.urls') ),
    path('home/Feedback/',include('feedback.urls') ),

    path('food/',include('Food.urls') ),
    path('home/food/',include('Food.urls') ),

    path('beauty/',include('beauty.urls') ),
    path('home/beauty/',include('beauty.urls') ),

   




]
