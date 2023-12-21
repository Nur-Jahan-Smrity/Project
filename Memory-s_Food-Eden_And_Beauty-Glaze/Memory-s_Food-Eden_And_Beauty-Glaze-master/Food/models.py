from django.db import models

Cake_Name = (
    ('Vanilla Cake','Vanilla Cake'),
    ('Strawbery Cake','Strawbery Cake'),
    ('Chocolate Cake','Chocolate Cake'),
    
)


Dessert_Name = (
    ('Nowabi Shemai','Nowabi Shemai'),
    ('Pastry','Pastry'),
    ('Yogurt','Yogurt'),
    
)

SpicyFood_Name = (
    ('Pasta','Pasta'),
    ('Halim','Halim'),
    ('Biryani','Biryani'),
    
)

Sweets_Name = (
    ('Khir Mohon','Khir Mohon'),
    ('Sponge Mishti','Sponge Mishti'),
    ('Rashmalay','Rashmalay'),
    ('Pasta','Pasta'),
    ('Halim','Halim'),
    ('Biryani','Biryani'),
    
)


Payment_way = (
    ('Bkash(01869537592)','Bkash(01869537592)'),
    ('Rocket(01869537592)','Rocket(01869537592)'),
    ('Cash On Delivery','Cash On Delivery'),
    
)

Cake_Quantity =(
    ('Half pound','Half pound'),
    ('1 pound','1 pound'),
    ('2 pound','2 pound'),
    ('3 pound','3 pound'),
    ('4 pound','4 pound'),
    ('5 pound','5 pound'),
    
)


Quantity =(
    ('500 ml','500 ml'),
    ('1000 ml','1000 ml'),
    ('1 kg','1 kg'),
    ('2 kg','2 kg'),
    ('3 kg','3 kg'),
    
)

class CakeOrder(models.Model):
    
    Username=models.CharField(max_length=50)
    PhoneNum=models.PositiveIntegerField()
    Email=models.EmailField()
    FoodName = models.CharField(choices=Cake_Name, max_length=50)
    Payment = models.CharField(choices=Payment_way , max_length=50)
    food_Quantity = models.CharField(choices=Cake_Quantity , max_length=50)
    Textarea=models.TextField()
    
    def __str__(self):
        return self.Username

class DessertOrder(models.Model):
    
    Username=models.CharField(max_length=50)
    PhoneNum=models.PositiveIntegerField()
    Email=models.EmailField()
    FoodName = models.CharField(choices=Dessert_Name, max_length=50)
    Payment = models.CharField(choices=Payment_way , max_length=50)
    food_Quantity = models.CharField(choices=Quantity , max_length=50)
    Textarea=models.TextField()
    
    def __str__(self):
        return self.Username



class SpicyOrder(models.Model):
    
    Username=models.CharField(max_length=50)
    PhoneNum=models.PositiveIntegerField()
    Email=models.EmailField()
    FoodName = models.CharField(choices=SpicyFood_Name, max_length=50)
    Payment = models.CharField(choices=Payment_way , max_length=50)
    food_Quantity = models.CharField(choices=Quantity , max_length=50)
    Textarea=models.TextField()
    
    def __str__(self):
        return self.Username


class SweetOrder(models.Model):
    
    Username=models.CharField(max_length=50)
    PhoneNum=models.PositiveIntegerField()
    Email=models.EmailField()
    FoodName = models.CharField(choices=Sweets_Name, max_length=50)
    Payment = models.CharField(choices=Payment_way , max_length=50)
    food_Quantity = models.CharField(choices=Quantity , max_length=50)
    Textarea=models.TextField()
    
    def __str__(self):
        return self.Username