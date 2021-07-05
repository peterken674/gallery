from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Image

def index(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images':images,})

def search(request):

    search_term = 'Travel'
    found_category = Category.objects.filter(name=search_term).first()
    found_images = Image.search_image(found_category)