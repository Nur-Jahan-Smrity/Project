from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

def about(request):
    return render(request,"About.html")

