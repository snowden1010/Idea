from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def home(request):
    return redirect("products:home-page")

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['first-name']
        lastname = request.POST['last-name']
        username = request.POST['username']
        email = request.POST['email'] 
        password = request.POST['password']
        c_password = request.POST['confirm-password']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username Already Used")
            return redirect("signup")
        
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already Used")
            return redirect("signup")

        else:
            if password == c_password and password is not None:
                user = User.objects.create_user(username, email, password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                messages.success(request, f"{username} Created Successfully!")
                return redirect("signin")
            
            else:
                messages.info(request, "Passwords don't match!")
                return redirect("signup")
        
    
    else:    
        return render(request, "authentication/signup.html")




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"{username} Logged In Successfully!")
            fname = user.first_name
            return redirect("products:home-page")
        
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("home")


    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")