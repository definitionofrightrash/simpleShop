from django.shortcuts import render
from .models import Customer
import hashlib
def index(request):
    return render(request,'Eshopper/login.html',{})
def register(request):
    username = request.POST['Name']
    email = request.POST['Email Address']
    password = request.POST['Password']
    if(username.strip() == "" or password.strip() == "" or Customer.objects.filter(Email  = email)):
        return render(request,"Eshopper/login.html")
    else: 
        c = Customer(Name = username, Email = email, Password = hashlib.md5(password.encode()))
        c.save()
        return render(request,'Eshopper/shop.html',{'Customer':c})
        
#def login(request):
   
