from django.http import HttpResponse
from django.shortcuts import render
from .models import ContactUs
from django.contrib import messages


def contactus(request):
    return render(request,"Contact.html")
    
def Contact(request):
    if request.method=="POST":
        Username =request.POST['Username']
        Email =request.POST['Email']
        Textarea =request.POST['Textarea']

        ContactUs(Username=Username,Email=Email,Textarea=Textarea).save()
        messages.success(request,'Thank you! We will contact you as soon as possible...')
        
       
        return render(request,"contact_us.html")
        
    else:
        return render(request,"contact_us.html")


