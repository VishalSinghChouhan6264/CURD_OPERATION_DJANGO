from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# from django.contrib.auth.decorators import login_required

# @login_required(login_url='login')
def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            return HttpResponse("your password and confirm password not equal")
        else:
            myuser=User.objects.create_user(uname,email,password1)
            myuser.save()
            return redirect("login")
    return render(request,"signup.html")

def loginpage(request):
    if request.method=='POST':
        uname1=request.POST.get('username')
        pass1=request.POST.get('pass')
        user = authenticate(request,username=uname1,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("username or password is not correct")
        
    return render(request,'login.html')

def homepage(request):
    return render(request,"home.html")

def Logout(request):
    logout(request)
    return redirect("login")