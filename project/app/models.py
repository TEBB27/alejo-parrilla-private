from django.db import models

# Create your models here.
from django.db import models

CATEGORY = [
    ('Carnes', 'Carnes'),
    ('Pescados', 'Pescados'),
    ('Típicos', 'Típicos'), 
    ('Bowls', 'Bowls'),
    ('Menú Infantil', 'Menú Infantil'),
]

RESTAURANTS = [
    ('Carnes', 'Carnes'),
    ('Pescados', 'Pescados'),
    ('Típicos', 'Típicos'), 
]
class menu (models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length =1000)
    category = models.CharField(choices = CATEGORY, max_length = 1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu', null=True, blank=True)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class contact(models.Model):
    email = models.EmailField()
    
class booking (models.Model):
    restaurant = models.CharField(choices=RESTAURANTS,  max_length = 1000)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    date = models.DateField()
    time = models.TimeField()
    seats = models.IntegerField()
    def __str__(self):
        return self.name

class recomendation(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length =1000)
    image = models.ImageField(upload_to='recomendation', null=True, blank=True)
    def __str__(self):
        return self.name