from django.shortcuts import render
from .models import Customer,Product
import hashlib
def index(request):
    p = Product.objects.all()
    return render(request,'Eshopper/shop.html',{'Products':p})
def loginPage(request):
    return render(request, 'Eshopper/login.html',{})
def register(request):
    username = request.POST['Name']
    email = request.POST['Email Address']
    password = request.POST['Password']
    if(username.strip() == "" or password.strip() == "" or Customer.objects.filter(Email  = email)):
        return render(request,"Eshopper/login.html")
    else: 
        c = Customer(Name = username, Email = email, Password = hashlib.md5(password.encode()).digest())
        c.save()
        p = Product.objects.all()
        return render(request,'Eshopper/shop.html',{'Products':p})
 
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        c = Customer.objects.get(Email = email , Password = hashlib.md5(password.encode()).digest())          
        p = Product.objects.all() 
        return render(request,'Eshopper/shop.html',{'Products':p})
    except Customer.DoesNotExist:
        return render(request, 'Eshopper/login.html',{})



