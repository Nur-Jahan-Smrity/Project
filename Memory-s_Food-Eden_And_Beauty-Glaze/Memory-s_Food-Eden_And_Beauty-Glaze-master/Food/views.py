from django.http import HttpResponse
from django.shortcuts import redirect, render
from.models import  CakeOrder, DessertOrder,SpicyOrder,SweetOrder
#from.models import  CakeOrder, DessertOrder,SpicyFood,Sweetorder
from django.contrib import messages



def foodpage(request):
    return render(request,"button.html")

def Cakes(request):
    return render(request,"c_menu.html")

def Dessert(request):
    return render(request,"dessert.html")

def SpicyFood(request):
    return render(request,"spicy.html")

def Sweets(request):
    return render(request,"sweet.html")

def Calculatec(request):
    return render(request,"Calculate1.html")

def Calculated(request):
    return render(request,"Calculate2.html")

def Calculates(request):
    return render(request,"Calculate3.html")
    
def Calculatess(request):
    return render(request,"Calculate4.html")


def Cake_Order(request):

    if request.method == 'POST':
        
        Username =request.POST['Username']
        PhoneNum = request.POST['PhoneNum']
        Email = request.POST['Email']
        FoodName = request.POST['FoodName']
        Payment =request.POST['Payment']
        food_Quantity = request.POST['food_Quantity']
        Textarea = request.POST['Textarea']
        
        #Check for error
        #FoodOrder(Username=Username, PhoneNum=PhoneNum,Email=Email,
        #FoodName=FoodName,Payment=Payment,food_Quantity=food_Quantity,Textarea=Textarea).save()

        CakeOrder(Username=Username, PhoneNum=PhoneNum,Email=Email,
        FoodName=FoodName,Payment=Payment,food_Quantity=food_Quantity,Textarea=Textarea).save()


        messages.success(request,'Order Confirmed! Very soon you will get the confirmation letter through gmail. ')
        return render(request,"food_order.html")
    else:
        return render(request,"food_order.html")

    

def Dessert_Order(request):
    if request.method == 'POST':
        
        Username =request.POST['Username']
        PhoneNum = request.POST['PhoneNum']
        Email = request.POST['Email']
        FoodName = request.POST['FoodName']
        Payment =request.POST['Payment']
        food_Quantity = request.POST['food_Quantity']
        Textarea = request.POST['Textarea']
        
        #Check for error

        DessertOrder(Username=Username, PhoneNum=PhoneNum,Email=Email,
        FoodName=FoodName,Payment=Payment,food_Quantity=food_Quantity,Textarea=Textarea).save()
        messages.success(request,'Order Confirmed! Very soon you will get the confirmation letter through gmail. ')
        return render(request,"newOrder.html")
    else:
        return render(request,"newOrder.html")



def Spicy_Order(request):
    if request.method == 'POST':
        
        Username =request.POST['Username']
        PhoneNum = request.POST['PhoneNum']
        Email = request.POST['Email']
        FoodName = request.POST['FoodName']
        Payment =request.POST['Payment']
        food_Quantity = request.POST['food_Quantity']
        Textarea = request.POST['Textarea']
        
        #Check for error

        SpicyOrder(Username=Username, PhoneNum=PhoneNum,Email=Email,
        FoodName=FoodName,Payment=Payment,food_Quantity=food_Quantity,Textarea=Textarea).save()
        messages.success(request,'Order Confirmed! Very soon you will get the confirmation letter through gmail. ')
        return render(request,"Spicy_Food.html")
    else:
        return render(request,"Spicy_Food.html")



def Sweet_order(request):
    if request.method == 'POST':
        
        Username =request.POST['Username']
        PhoneNum = request.POST['PhoneNum']
        Email = request.POST['Email']
        FoodName = request.POST['FoodName']
        Payment =request.POST['Payment']
        food_Quantity = request.POST['food_Quantity']
        Textarea = request.POST['Textarea']
       
        #Check for error

        SweetOrder(Username=Username, PhoneNum=PhoneNum,Email=Email,
        FoodName=FoodName,Payment=Payment,food_Quantity=food_Quantity,Textarea=Textarea).save()
        messages.success(request,'Order Confirmed! Very soon you will get the confirmation letter through gmail. ')
        return render(request,"Sweet_order.html")
    else:
        return render(request,"Sweet_order.html")


def Calculate(request):
    return render(request,"Calculate.html")
