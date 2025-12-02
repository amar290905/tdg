from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def places(request):
    return render(request, 'places.html')

def packages(request):
    return render(request, 'packages.html')

def contact(request):
    return render(request, 'contact.html')

