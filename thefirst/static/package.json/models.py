from django.db import models
from datetime import datetime
from realtors.models import Realtor
# Create your models here.
class Listing(models.Model):
    realtor_id=  models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)#on_delete to tell what to do with Listing 
    # when realtor_id is deleted
    title= models.CharField(max_length=200)
    adress= models.CharField(max_length=200)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    zipcode= models.CharField(max_length=20)
    description= models.TextField(blank=True)##blank= true makes it optional on creation
    price= models.IntegerField()
    bedrooms= models.IntegerField()
    bathrooms= models.DecimalField(max_digits=2,decimal_places=1)
    garage= models.IntegerField(default=0)
    square_feet= models.IntegerField()
    lot_size= models.DecimalField(max_digits=5,decimal_places=1)
    image_main= models.ImageField(upload_to='photos/%Y/%m/%d/')##stored inside Media Folder and stored by year month and day! 
    image_1= models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image_2= models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image_3= models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image_4= models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image_5= models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    image_6= models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published = models.BooleanField(default=True)
    date_published = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.title