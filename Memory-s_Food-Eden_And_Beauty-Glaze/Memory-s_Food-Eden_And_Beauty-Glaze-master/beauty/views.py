from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from.models import  Beauty

def beauty(request):
    return render(request,"beauty.html")
def calculator(request):
    return render(request,"calculator.html")

def ordercart(request):

    if request.method == 'POST':
        
        Username =request.POST['Username']
        PhoneNum = request.POST['PhoneNum']
        Email = request.POST['Email']
        Payment =request.POST['Payment']
        Textarea = request.POST['Textarea']
        
        #Check for error
        
        Beauty(Username=Username, PhoneNum=PhoneNum,Email=Email,
        Payment=Payment,Textarea=Textarea).save()
        messages.success(request,'Order Confirmed! Very soon you will get the confirmation letter through gmail. ')
        
        return render(request,"finalchck.html")
    else:
        return render(request,"finalchck.html")
       

def finalchck(request):
    return render(request,"ordercart.html")
   
