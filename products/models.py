from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254) 
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category',null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)   #required
    description = models.TextField()                                 #required
    price = models.DecimalField(max_digits=6,decimal_places=2)       #required
    rating = models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True)
    image_url = models.URLField(max_length=1024,null=True,blank=True)
    image =models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
    