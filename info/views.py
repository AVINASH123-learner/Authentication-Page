# Importing redirect library from django
from django.shortcuts import render,redirect
# Importing Authentication luibrary of Django
from django.contrib.auth.models import User
# Importing messages library of django
from django.contrib import messages
# To authenticate for valid user on sign in
from django.contrib.auth import authenticate
# To check if the user is a valid user or not
from django.contrib.auth import login
# To check logout current user
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request, "index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
  
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request,"Your account has been successfully created")

        return redirect(signin)

    return render(request, "signup.html")

def signin(request):
    if request.method=="POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass1")

        user = authenticate(username=username, password=pass1)

        # If user is a valid user
        if user is not None:
            fname = user.first_name
            login(request,user)
            return render(request, 'index.html',{"fname":fname})
        # If user credentials are Incorrect
        else:
            messages.error(request,"Bad Credentials!")
            return redirect(index)

    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request,"logged out Sucessfuly")
    return redirect(index)