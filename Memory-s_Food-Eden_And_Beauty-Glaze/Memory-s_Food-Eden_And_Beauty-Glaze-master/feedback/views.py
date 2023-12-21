from django.http import HttpResponse
from django.shortcuts import render
from .models import Feedback
from django.contrib import messages

def Feedbackpage(request):
    if request.method=="POST":
        Username =request.POST['Username']
        Email =request.POST['Email']
        Textarea =request.POST['Textarea']

        Feedback(Username=Username,Email=Email,Textarea=Textarea).save()
        messages.success(request,'Thank you for your feedback...')
        
       
        return render(request,'feedback.html')
        
    else:
      return render(request,'feedback.html')

   
    
