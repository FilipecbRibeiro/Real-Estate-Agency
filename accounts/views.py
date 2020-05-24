from django.shortcuts import redirect, render
from django.contrib import messages,auth
# Create your views here.
from django.contrib.auth.models import User#### IMPORTING OUR USER !!!!!
from contacts.models import Contact
def register(request):
    if request.method=='POST':
      # GET FORM VALUES
      first_name= request.POST['first_name']
      last_name= request.POST['last_name']
      username= request.POST['username']
      email= request.POST['email']
      password= request.POST['password']
      password2= request.POST['password2']
      
      ##### LET'S CHECK SOME VALIDATION ####### 
      if password == password2:### CHECKING IF PASSWORDS MATCHES
          if User.objects.all().filter(username=username).exists():#### IS USERNAME BEING INTRODUCED ALREADY EXISTS IN OUR DB ?
              messages.error(request,'Username already exists!')
              return redirect('register')
          
          
          else:
             if User.objects.all().filter(email=email).exists():#### IS EMAIL BEING INTRODUCED ALREADY EXISTS IN OUR DB ?
                messages.error(request,'Email already exists!')
                return redirect('register')
             else:### EVERYTHING CHECKED OUT!!!!!!!
                 #### CREATE A USER WITH INFO COMING FROM REGISTER.HTML FORM
                new_user= User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                ### IF WE WANT LOG IN RIGHT AFTER THE CREATION OF USER :
                    #auth.login(request,new_user)
                    #messages.success(request,'Your are now logged in ')
                    #return redirect('index')
                ### Saving into db and redirect into login
                new_user.save()
                messages.success(request,'You are now register you can login')
                return redirect('login')
      else:
          messages.error(request,'Passwords not equal')
          return redirect('register')
      
    return render(request, 'accounts/register.html')



##################### HANDLE LOGIN ###################################
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        test_user= auth.authenticate(username=username,password=password)
        
        if test_user is not None:
            auth.login(request,test_user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Wrong Credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You have successfully logged out')
        return redirect('index')
    return render(request,'accounts/logout.html')
def dashboard(request):
    contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    
    context={
        'contacts': contacts
    }
    
    
    return render(request, 'accounts/dashboard.html',context)

