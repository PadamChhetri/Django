from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  peoples =[
    {'name':"Padam Chhetri",'age':20},
    {'name':"Adam chhetri",'age':17},
    {'name':"Deepak chhetri",'age':19},
    {'name':"Viki chhetri",'age':24}
  ]
  
  vegetables=['Pumpkin','Tomato','Potato']
  # for people in peoples:
  #   print(people) #print in terminal

  
  return render(request, "index.html",context={'title': "DjangoCourse",'peoples':peoples,'Vegetables':vegetables}) #Connect index.html  and used context to provide django data into html templates
  
def about(request):
  context={'title':'About'}
  return render(request, "about.html",context)

def contact(request):
  context={'title':'Contact'}
  return render(request, "contact.html",context)

def success_page(request):
  print("*" *10)
  return HttpResponse("<h1> Hey, this is the success page </h1>")