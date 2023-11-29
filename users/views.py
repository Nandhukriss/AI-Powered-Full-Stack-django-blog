from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('view_post')
        else:
            messages.error(request, 'Incorrect username or password')
        
    return render(request,"login.html")


def user_register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        # Check for uniqueness of both username and email
        if not User.objects.filter(Q(username=uname) | Q(email=email)).exists():
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        else:
            messages.error(request, 'Username or email already exists. Please choose different credentials.')
    return render(request,"register.html")

def logout_user(request):
    logout(request)
    return redirect('view_post')