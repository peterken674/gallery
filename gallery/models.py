from django.db import models

class Image(models.Model):
    '''Class to define attributes of an image in the gallery, and it's methods.
    '''
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    post_date = models.DateTimeField(auto_now_add=True)


class Location(models.Model):
    '''Class to define the location of a photo in the gallery.
    '''
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Category(models.Model):
    '''Class to define the category of an image on the gallery.
    '''
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
