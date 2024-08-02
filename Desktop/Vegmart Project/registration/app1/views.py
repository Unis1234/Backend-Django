from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from decimal import Decimal, InvalidOperation
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home1.html')

def SignupPage(request):
    if request.method=='POST':
        email=request.POST.get('username')
        dob=request.POST.get('date')
        adress=request.POST.get('adress')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            messages.warning(request,"Password is Incorrect")
            return redirect('/SignupPage')
        try:
           if User.objects.get(username=email):
                messages.warning(request,"User is Taken")
                return redirect('/SignupPage')
        except:
           pass
        
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email is Taken")
                return redirect('/SignupPage')
        except:
           pass
        
        my_user=User.objects.create_user(email,email,pass1)
        my_user.save()
        messages.info(request,"Signup Success Please Login")
        return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, "Invalid Credentaimls ")
            return redirect('/')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
# Create your views here.
def home(request):
    return render(request,"home.html")




 
