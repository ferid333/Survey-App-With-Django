from distutils.log import error
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from surveys.models import Survey
# Create your views here.
def index(request):
    request.session['visits']=[]
    return render(request,"base.html")
def login_request(request):
    if request.user.is_authenticated :
        return redirect("home")
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
          login(request,user)
          return redirect("home")
        else:
           return render(request,"account/login.html",{
                "error":"Password or username is false"
             })
    return render(request,"account/login.html") 
def logout_request(request):
        logout(request)
        return redirect("home")
def register_request(request):
    if request.user.is_authenticated :
        return redirect("home")
    if request.method=="POST":
       username=request.POST["username"]
       email=request.POST["email"]
       password=request.POST["password"]
       if User.objects.filter(username=username).exists():
            context={
                "username":"",
               " email":email,
               " password":password,
                "error":"Username exist"
            }
            return render(request,"account/register.html",context)
       elif User.objects.filter(username=username).exists():
            context={
                "username":username,
               " email":"",
                "password":password,
               " error":"Email exist" 
            }
            return render(request,"account/register.html",context)  
       else:
        new_user=User.objects.create(username=username,email=email)
        new_user.set_password(password)
        new_user.save()
        return redirect("login") 
    return render(request,"account/register.html")            