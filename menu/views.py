from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Coffee, Snack

def home(request):
    return render(request, 'index.html')

def add_coffee(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Coffee.objects.create(name=name, description=description, price=price)
        return redirect('home')
    return render(request, 'adding_new_coffee.html')

def add_snack(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        Snack.objects.create(name=name, description=description, price=price)
        return redirect('home')
    return render(request, 'adding_new_snack.html')
