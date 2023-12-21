from django.db import models

class Feedback(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.EmailField()
    Textarea=models.TextField()
    
    def __str__(self):
        return self.Username