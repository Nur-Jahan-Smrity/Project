from django.db import models



Payment_way = (
    ('Bkash(01869537592)','Bkash(01869537592)'),
    ('Rocket(01869537592)','Rocket(01869537592)'),
    ('Cash On Delivery','Cash On Delivery'),
  )



class Beauty(models.Model):
    
    Username=models.CharField(max_length=50)
    PhoneNum=models.PositiveIntegerField()
    Email=models.EmailField()
    Payment = models.CharField(choices=Payment_way , max_length=50)
    Textarea=models.TextField()
    
    def __str__(self):
        return self.Username