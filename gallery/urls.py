from django.urls import path

from . import views 

'''Defining the route urls.
'''
urlpatterns = [
    path('', views.index, name='index'),
]