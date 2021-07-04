from django.db import models

class Location(models.Model):
    '''Class to define the location of a photo in the gallery.
    '''
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def save_location(self):
        '''Method to save the location to the database.
        '''
        self.save()

    def delete_location(self):
        '''Method to delete the location from the database.
        '''
        self.delete()

    def update_location(self, name, country):
        '''Method to update the location in the database.
        '''
        location = Location.objects.get(name=self.name)
        location.name = name
        location.country = country
        location.save()

    def __str__(self):
        return self.name

class Category(models.Model):
    '''Class to define the category of an image on the gallery.
    '''
    name = models.CharField(max_length=150)

    def save_category(self):
        '''Method to save the category to the database.
        '''
        self.save()

    def delete_category(self):
        '''Method to delete the category from the database.
        '''
        self.delete()

    def update_category(self, name):
        '''Method to update the category in the database.
        '''
        category = Category.objects.get(name=self.name)
        category.name = name
        category.save()

    def __str__(self):
        return self.name

class Image(models.Model):
    '''Class to define attributes of an image in the gallery, and it's methods.
    '''
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        '''Method to save the image to the database.
        '''
        self.save()

    def delete_image(self):
        '''Method to delete the image from the database.
        '''
        self.delete()

    def update_image(self, image, name, description, location, category):
        '''Method to update the image in the database.
        '''
        image = Image.objects.get(name=self.name)
        image.name = name
        image.save()

    @classmethod
    def get_image_by_id(cls, id):
        '''Allows us to get an image using its ID.
        '''
        return cls.objects.filter(id=id)

    @classmethod
    def search_image(cls, category):
        '''Allows us to search for an image using its category.
        '''
        return cls.objects.filter(category=category)

    classmethod
    def filter_by_location(cls, location):
        '''Allows us to filter images by the location.
        '''
        return cls.objects.filter(location=location)


