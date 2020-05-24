from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
def receive_form_inquiry(request):
    if request.method=='POST':
        
        listing_id= request.POST['listing_id']
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        message= request.POST['message']
        listing= request.POST['listing']
        realtor_email= request.POST['realtor_email']
        user_id=request.POST['user_id']
        
        
        ## Check if the user has made already an inquiry!! 
    
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted= Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
               
                messages.error(request,'YOu have already made an inquiry for this listing')
                return redirect('/listings/'+ listing_id)
                
        
        
        
        contact= Contact(listing= listing, listing_id= listing_id, name=name,email=email,
                         phone=phone,message_content=message,user_id= user_id)
             
        contact.save()
        
        ###### send mail part! 
        send_mail(
            'Propert Listing Inquiry' , #### subject
            'There has been an inquiry for ' + listing +'.Sign into the admin panel for more info ',
            'testemailonwebd@gmail.com',
            [realtor_email,'filipecbribeiro@gmail.com'],
            fail_silently=False
        )
        messages.success(request,'Your request have been submitted, a realtor will get back to'
                         +'you soon as possible')
    return redirect('/listings/' + listing_id)