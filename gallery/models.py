from django.db import models
from cloudinary.models import CloudinaryField

class Location(models.Model):
    '''Class to define the location of a photo in the gallery.
    '''
    name = models.CharField(max_length=200)

    def save_location(self):
        '''Method to save the location to the database.
        '''
        self.save()

    def delete_location(self):
        '''Method to delete the location from the database.
        '''
        self.delete()

    @classmethod
    def update_location(cls, id, name):
        '''Method to update the location in the database.
        '''
        return cls.objects.filter(id=id).update(name=name)

    def __str__(self):
        return self.name

class Category(models.Model):
    '''Class to define the category of an image on the gallery.
    '''
    name = models.CharField(max_length=200)

    def save_category(self):
        '''Method to save the category to the database.
        '''
        self.save()

    def delete_category(self):
        '''Method to delete the category from the database.
        '''
        self.delete()

    @classmethod
    def update_category(cls, id, name):
        '''Method to update the category in the database.
        '''
        return cls.objects.filter(id=id).update(name=name)

    def __str__(self):
        return self.name

class Image(models.Model):
    '''Class to define attributes of an image in the gallery, and it's methods.
    '''
    # image = models.ImageField(upload_to='images/', null=True)
    image = CloudinaryField('image', null=True)
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        '''Method to save the image to the database.
        '''
        self.save()

    def delete_image(self):
        '''Method to delete the image from the database.
        '''
        self.delete()

    @classmethod
    def update_image(cls, id, image):
        '''Method to update the image in the database.
        '''
        return cls.objects.filter(id=id).update(image=image)
        

    @classmethod
    def get_image_by_id(cls, id):
        '''Allows us to get an image using its ID.
        '''
        return cls.objects.filter(id=id).all()

    @classmethod
    def search_image(cls, search_term):
        '''Allows us to search for an image using its category.
        '''
        category = Category.objects.get(name__icontains=search_term)
        return cls.objects.filter(category=category).all()

    @classmethod
    def filter_by_location(cls, location):
        '''Allows us to filter images by the location.
        '''
        return cls.objects.filter(location=location).all()


