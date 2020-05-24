from django.contrib import admin

# Register your models here.
from .models import Listing#### (class model of listing)

class ChangeListingDisplay(admin.ModelAdmin):
    list_display =('id','title','price','realtor_id','is_published','date_published')
    list_display_links=('id', 'title')
    list_filter = ('realtor_id',)
    list_editable= ('is_published', 'date_published')
    search_fields=('title', 'description', 'adress', 'city', 'state', 'zipcode', 'price')
    list_per_page= 5
admin.site.register(Listing,ChangeListingDisplay)