from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views 

'''Defining the route urls.
'''
urlpatterns = [
    path('', views.index, name='index'),
    path('kenya/', views.location_kenya, name='location_kenya'),
    path('togo/', views.location_togo, name='location_togo'),
    path('sierra/', views.location_sierra, name='location_sierra'),
    path('egypt/', views.location_egypt, name='location_egypt'),
    path('search/', views.search_results, name='search_results'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)