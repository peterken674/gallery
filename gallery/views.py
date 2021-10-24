from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework import serializers
from .models import Category, Image, Location
from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ImageSerializer


images = []
def index(request):
    global images
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

def search_results(request):
    
    if 'search' in request.GET and request.GET['search']:
        global images
        search_term = request.GET.get('search')
        message = f"{search_term}"
        try:
            images = Image.search_image(search_term)
            if not images:
                message = f'No results found for category "{search_term}". Please try  the search again from among the provided choices.'
        except Image.DoesNotExist:
            raise Http404()
        return render(request, 'index.html', {'images':images, 'message':message,})

    else:
        message = "You haven't searched for any term"
        return render(request, 'index.html', {'images':images, "message":message})


# API
class ImagesList(APIView):
    def get(self, request, format=None):
        all_images = Image.objects.all()
        serializers = ImageSerializer(all_images, many=True)
        return Response(serializers.data)