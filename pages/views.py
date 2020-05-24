from django.shortcuts import render
#from django.http import HttpResponse
from django.template import Context
# Create your views here.

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices,price_choices, states_choices
def index(request):
    listings = Listing.objects.order_by('-date_published').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'bedroom_choices': bedroom_choices,
        'price_choices':price_choices,
        'state_choices':states_choices,
    }
    print(len(states_choices))
    return render(request,'pages/index.html',context) 
def about(request):
    #Get all realtors
    realtors= Realtor.objects.order_by('-hire_date')
    #Get MVP 
    emp_month = Realtor.objects.all().filter(is_emp_month = True)
    print(len(emp_month))
    context= {
        'realtors':realtors,
        'emp_month': emp_month
        
    }
    return render(request,'pages/about.html',context)
def smth(request):
    return render(request,'smtg.html')