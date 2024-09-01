from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    #check to see if the person is logging in 
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        
        #Authenticate
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You Have Successfully Logged In!")
            return redirect('home')
        else:
            messages.success(request, "There was An Error Logging In......., Please Try Again........")
            return redirect('home')
    else:
        return render(request,'website/home.html')

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out.....")
    return redirect('home')

def register_user(request):
    return render(request, 'website/register.html',{})