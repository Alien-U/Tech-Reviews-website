from django.shortcuts import render
from django.http import HttpResponse
from.models import product,Softwarez,Gaming,Contact
from math import ceil
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
    # n=len(products)
    # after added
    # nSlides=n//4 + ceil((n/4)-(n//4))
    # ----------*--------------
    params={'Product':products}
    # print(products)
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
    #fetch the product using id
    products=product.objects.filter(id=myid)
    # print(products)
    return render(request,'shome/prodview.html',{'product':products[0]})

def softview(request,myid):
    #fetch the product using id
    softwares=Softwarez.objects.filter(id=myid)
    return render(request,'shome/softwareview.html',{'Softwarez':softwares[0]})
    
def gameview(request,myid):
    #fetch the product using id
    games=Gaming.objects.filter(id=myid)
    return render(request,'shome/gameview.html',{'Gaming':games[0]})
    
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        message=request.POST.get('message','')
        contact=Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request,'shome/contact.html')