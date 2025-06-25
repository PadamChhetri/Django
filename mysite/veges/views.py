from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse

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

  
