from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, default='')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, default='')
    
    STATUS = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Average', 'Average'),
        ('Poor', 'Poor')
    )
    Rate_our_Products_and_services = models.CharField(max_length=15, choices=STATUS, blank=True, default='-----')
    
    Give_Your_Valuable_Feedback = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.name