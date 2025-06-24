from django.shortcuts import render , redirect
from .models import *

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
  return render(request,"receipe.html")