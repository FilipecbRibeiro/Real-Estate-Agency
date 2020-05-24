from django.db import models
from django.db import models
from datetime import datetime
# Create your models here.
class Contact(models.Model):
    listing= models.CharField(max_length=200)
    listing_id= models.IntegerField()
    name= models.CharField(max_length=200)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    message_content=models.TextField(blank=True)
    contact_date= models.DateTimeField(default=datetime.now,blank=True)
    user_id= models.IntegerField(blank=True)
    ### optionally because we want to allow unregister users to also be able to make inqueries!! 
    ### but we have to sso we can show in user dashboard in case they are registered!
    
    
  
    def __str__(self):
        return self.name