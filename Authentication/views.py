from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib import auth


# Create your views here.
def signUp(request):
    if(request.method == "POST" and "username" in request.POST.keys() and "password" in request.POST.keys() ):
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(username,email,password)
        print("Created")
        user = authenticate(username = username, password = password)
        if(user.is_authenticated):
            auth.login(request,user)
            return HttpResponseRedirect("home")
        else:
            context = {
                "text" : "Sign Up Failed. Try Again"
            }
            return render(request,"signup.html",context)
    else:
        return render(request,"signup.html",{})

def login(request):
    if(request.method == "POST" and request.POST["username"] and request.POST["password"] ):
        print("In")
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        print()
        if(user != None): 
            auth.login(request,user)
            return HttpResponseRedirect("home")
        else:
            context = {
                "text" : "Login Failed. Please Try again"
            }
            return render(request,"login.html",context)
    else:
        return render(request,"login.html",{})

def home(request):
    if(request.user.is_authenticated):
        context = {
            "text" : "Welcome"
        }
        return render(request,"home.html",context)
    else:
        return render(request,"home.html",{}) 

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

        