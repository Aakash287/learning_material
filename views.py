from django.shortcuts import render,redirect
from .models import Details
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
# Create your views here.
def signup(request):
    if request.method=="POST":
        name=request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        number = request.POST["number"]
        address = request.POST["address"]
        image = request.FILES["image"]
        file = request.FILES["file"]
        Details(name=name,email=email,password=password,number=number,address=address,image=image,file=file).save()
    return render(request,'sign_up.html')

def login(request):
    if request.method=='POST':
        email=request.POST["email"]
        password=request.POST["password"]
        print(email)
        print(password)
        try:
            t=Details.objects.get(email=email,password=password)
            print(email)
            print(password)
            return redirect('/home/')

        except:
            print(email)
            print(password)
            return redirect('/login/')
        print("done")
    return render(request,'login.html')

def home(request):
    data=Details.objects.all()
    return render(request,'home.html',{'data':data})

def update(request, id):
    x= Details.objects.get(id=id)

    if request.method == 'POST':
        x.name=request.POST['name']
        x.email = request.POST['email']
        x.number = request.POST['number']
        x.address = request.POST['address']
        x.save()
    return render(request, 'update.html', {'x':x})

    # template = loader.get_template(update.html)
    # context={
    #     'mymember' : mymember,
    # }

def delete(request, id):
    y=Details.objects.get(id=id)
    y.delete()
    return redirect('/home/')
    
    
    
    
    from django.db import models



class Details(models.Model):

    name= models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=200)
    number=models.BigIntegerField()
    address=models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/', null=True)
    image = models.ImageField(upload_to='images/', null=True)
    
    
    
    
    
    
