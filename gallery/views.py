from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Image, Location

def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images':images,})

def location_kenya(request):
    location_kenya = Location.objects.get(name='Kenya')
    images = Image.objects.filter(location=location_kenya)
    return render(request, 'index.html', {'images':images,})
def location_togo(request):
    location_togo = Location.objects.get(name='Togo')
    images = Image.objects.filter(location=location_togo)
    return render(request, 'index.html', {'images':images,})
def location_sierra(request):
    location_sierra = Location.objects.get(name='Sierra Leone')
    images = Image.objects.filter(location=location_sierra)
    return render(request, 'index.html', {'images':images,})
def location_egypt(request):
    location_egypt = Location.objects.get(name='Egypt')
    images = Image.objects.filter(location=location_egypt)
    return render(request, 'index.html', {'images':images,})