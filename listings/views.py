from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import bedroom_choices,states_choices,price_choices
# Create your views here.
def index(request):
    #listings = Listing.objects.all()
    listings= Listing.objects.order_by('-price').filter(is_published=True)
    paginator= Paginator(listings,6)
    page= request.GET.get('page')
    listing_paginator= paginator.get_page(page)
    context={
        'listings': listing_paginator
        
        
    }
    
    return render(request,'listings/listings.html',context)
    
    
'''
return render(request,'listings/listings.html',{
        
        'name':'filipe'## this part will be substitute by context variable!!!
    })

'''    

    
def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk = listing_id)
    
    context={'listing':listing}
    return render(request,'listings/listing.html',context)

def search(request):
    query_list= Listing.objects.order_by('-date_published')
 
    #for keywords coming from form;
    if 'keywords' in request.GET:
        keywords= request.GET['keywords']
        if keywords:
            print(keywords)
            query_list=query_list.filter(description__icontains=keywords)
    #for city coming from form;
    if 'city' in request.GET:
        city =request.GET['city']
        if city:
            query_list= query_list.filter(city__iexact=city)### exact(without 'i' in the beginning) if we want case sensitive!!!!
    #for state coming from form;
    if 'state' in request.GET:
        state =request.GET['state']
        if state:
            query_list= query_list.filter(state__iexact=state)
    #for state coming from form;
    if 'bedrooms' in request.GET:
        bedrooms =request.GET['bedrooms']
        if bedrooms:
            query_list= query_list.filter(bedrooms__lte=bedrooms)
    #for price coming from form;
    if 'price' in request.GET:
        price= request.GET['price']
        if price:
            query_list= query_list.filter(price__lte=price)
    context={
        'bedroom_choices' : bedroom_choices,
        'state_choices': states_choices,
        'price_choices': price_choices,
        'listings':query_list,
        'values': request.GET ## we are saving all our request values !
    }
    return render(request,'listings/search.html',context)
    