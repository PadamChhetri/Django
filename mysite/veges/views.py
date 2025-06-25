from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse

# Create your views here.

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
  context={'receipes':queryset}

  return render(request,"receipe.html",context)

def delete_receipe(request,id):
  queryset=Receipe.objects.get(id=id)
  queryset.delete()
  return redirect("/receipes/")

  
