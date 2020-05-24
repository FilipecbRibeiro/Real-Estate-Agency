from django.urls import path,include
from . import  views


urlpatterns = [
    path('',views.index,name='listings'),
    ##ideal our path will be  /listing/22
    path('<int:listing_id>',views.listing,name='listing'),
    path('search',views.search,name='search')
    
    #### WHY DON'T WE NEED TO ADD /listing/search' as first parameter???? 
    ############ BECAUSE WE ARE GOING TO LINK THIS TO OUR MAIN URL.PY SO WHENEVER THE URL
    ################## IS /listing/ WE KNOWS THIS IS THE FILE TO SEARCH

]