from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from.models import product,Softwarez,Gaming,Contact
from math import ceil
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    products=product.objects.all()
    # afteradded
    softwares=Softwarez.objects.all()
    games=Gaming.objects.all()
    # afterend
    params={'Product':products,'Softwarez':softwares,'Gaming':games}
    return render(request,'shome/index.html',params)

def gadgets(request):
    products=product.objects.all()
    # ----------*--------------
    params={'Product':products}
    return render(request,'shome/gadgets.html',params)

def software(request):
    softwares=Softwarez.objects.all()
    params={'Softwarez':softwares}
    return render(request,'shome/software.html',params)

def gaming(request):
    games=Gaming.objects.all()
    params={'Gaming':games}
    return render(request,'shome/gaming.html',params)

def about(request):
    return render(request,'shome/about.html')

def prodview(request,myid):
    softscroll=Softwarez.objects.all()
    prodscroll=product.objects.all()
    gamescroll=Gaming.objects.all()
    #fetch the product using id
    products=product.objects.filter(id=myid)
    params={'product':products[0],'Softscroll':softscroll,'Prodscroll':prodscroll,'Gamescroll':gamescroll}
    return render(request,'shome/prodview.html',params)

def softview(request,myid):
    softscroll=Softwarez.objects.all()
    prodscroll=product.objects.all()
    gamescroll=Gaming.objects.all()
    #fetch the product using id
    softwares=Softwarez.objects.filter(id=myid)
    params={'Softwarez':softwares[0],'Softscroll':softscroll,'Prodscroll':prodscroll,'Gamescroll':gamescroll}
    return render(request,'shome/softwareview.html',params)
    
def gameview(request,myid):
    softscroll=Softwarez.objects.all()
    prodscroll=product.objects.all()
    gamescroll=Gaming.objects.all()
    #fetch the product using id
    games=Gaming.objects.filter(id=myid)
    params={'Gaming':games[0],'Softscroll':softscroll,'Prodscroll':prodscroll,'Gamescroll':gamescroll}
    return render(request,'shome/gameview.html',params)
    
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request,'shome/contact.html')

def AccountPage(request):
    return render(request,'shome/LoginSignup.html')
def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Email = request.POST['Email'] 
        Password = request.POST['Password'] 
        #check for errorneous input
        #create the user
        myuser = User.objects.create_user(username,Email,Password)
        myuser.first_name = Fname
        myuser.last_name = Lname
        myuser.save()
        login(request, myuser)#login for authenticating user
        messages.success(request,"Your account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse("404-Not Found")

def handleLogin(request):
    if request.method=='POST':
        Loginusername=request.POST['Loginusername']
        LoginPass= request.POST['LoginPass'] 
        user=authenticate(username=Loginusername,password=LoginPass)
        if user is not None:
           login(request,user)
           messages.success(request,"successfully loggdin")
           return redirect('/')
        else:
           messages.error(request,"Invalid Credentials, Please try again")
           return redirect('/')   
    return HttpResponse("404-Not Found")

def handleLogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('/')
    # return HttpResponse("handleLogout")

#we will work on comments letter
