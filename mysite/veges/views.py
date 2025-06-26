from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login

# Add data.
def receipes(request):
  if request.method== "POST":
    data=request.POST #fetch data from receipe.html 
    
    image=request.FILES.get('image')
    receipe_name=data.get("receipe_name")
    description=data.get("description")

    Receipe.objects.create(
      image=image,
      receipe_name=receipe_name,
      description=description,
      )
    
    return redirect("/receipes")

  queryset= Receipe.objects.all() #Fetch all data from backend

#For search
  if request.GET.get('search'):
    queryset=queryset.filter(receipe_name__icontains=request.GET.get('search'))

  context={'receipes':queryset}
  return render(request,"receipe.html",context)


#Update Data
def update_receipe(request,id):
  queryset=Receipe.objects.get(id=id)

  if request.method=="POST":
    data=request.POST #fetch data from update_receipes.html
    image=request.FILES.get('image')
    receipe_name=data.get("receipe_name")
    description=data.get("description")

    queryset.receipe_name=receipe_name
    queryset.description=description
    if image:
      queryset.image=image
    queryset.save()
    return redirect("/receipes/")
  
  context={'receipe':queryset}
  return render(request,'update_receipes.html',context)


#Delete Data
def delete_receipe(request,id):
  queryset=Receipe.objects.get(id=id)
  queryset.delete()
  return redirect("/receipes/")

#login
#login
def login_page(request):
  if request.method == "POST":
    username=request.POST.get('username')
    password=request.POST.get('password')

    if not User.objects.filter(username=username).exists():
      messages.error(request, "Invalid Usename")  
      return redirect("/login/")

    user= authenticate(username=username,password=password)
    
    if user is None:
      messages.error(request, "Invalid Usename")  
      return redirect("/login/")
    else:
      login(request,user)
      return redirect("/receipes/")

  return render(request, 'login.html')


  
#Register
def register(request):
  if request.method == "POST":
    first_name=request.POST.get('first_name') #from register page name redirect
    last_name=request.POST.get('last_name')
    username=request.POST.get('username')
    password=request.POST.get('password')

    user=User.objects.filter(username=username)

    if user.exists():
      messages.info(request, "Usename already Taken")  
      return redirect("/register/")

    user=User.objects.create(
      first_name=first_name,
      last_name=last_name,
      username=username,
   )
    
    user.set_password(password)
    user.save()
    
    messages.success(request, "User registered successfully!")  

    return redirect("/register/")
  return render(request,'register.html')


def logout_page(request):
  logout(request)
  return redirect("/register/")
  