from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
  return render(request, "index.html") #Connect index.html 


def success_page(request):
  print("*" *10)
  return HttpResponse("<h1> Hey, this is the success page </h1>")