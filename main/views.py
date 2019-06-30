from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render

def comment(request):
    return render(request, "main/Comment/index.html")

def about(request):
    return render(request, "main/About/index.html")

def index(request):
    return render(request, "main/Main/index.html")

def doughnut(request):
    return render(request, "main/Doughnut/index.html")

def fruit(request):
    return render(request, "main/Fruit/index.html")

def product(request):
    return render(request, "main/Product/index.html")

def waffle(request):
    return render(request, "main/Waffle/index.html")

def yogurt(request):
    return render(request, "main/Yogurt/index.html")

def contact(request):
    return render(request, "main/Contact/index.html")

# Create your views here.
