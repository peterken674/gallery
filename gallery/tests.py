from django.test import TestCase
from .models import Image, Location
from .models import Category

class LocationTest(TestCase):
    def setUp(self):
        self.test_location = Location(name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_location, Location))

    def test_save_method(self):
        self.test_location.save_location()
        self.assertTrue(len(Location.objects.all()) > 0)

    def test_delete_method(self):
        self.test_location.save_location()
        self.assertTrue(len(Location.objects.all()) > 0)
        self.test_location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)

    def test_update_method(self):
        self.test_location.save_location()
        self.test_location.update_location(self.test_location.id, 'Nyeri')
        self.assertTrue(Location.objects.get(name='Nyeri').name, 'Nyeri')
        self.assertTrue(len(Location.objects.all())==1)

class CategoryTest(TestCase):
    def setUp(self):
        self.test_category = Category(name='pets')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_category, Category))

    def test_save_method(self):
        self.test_category.save_category()   
        self.assertTrue(len(Category.objects.all()) > 0)

    def test_delete_method(self):     
        self.test_category.save_category()
        self.assertTrue(len(Category.objects.all()) > 0)
        self.test_category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)

    def test_update_method(self):
        self.test_category.save_category()
        self.test_category.update_category(self.test_category.id, 'travel')
        self.assertTrue(Category.objects.get(name='travel').name, 'travel')
        self.assertTrue(len(Category.objects.all())==1)

class ImageTest(TestCase):
    '''Class to test the Image class.
    '''

    def setUp(self):
        self.nyeri = Location(name='Nyeri')
        self.nyeri.save_location()

        self.travel = Category(name='Travel')
        self.travel.save_category()

        self.cruising_image=Image(name='Falls',description='A waterfall',location=self.nyeri,category=self.travel)
        self.cruising_image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.cruising_image, Image))

    def test_save_method(self):
        self.cruising_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)

    def test_delete_method(self):     
        self.cruising_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)
        self.cruising_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update_method(self):
        self.cruising_image.save_image()
        self.cruising_image.update_image(self.cruising_image.id,image='media/test.png')
        self.assertEqual(Image.objects.get(image='media/test.png').image,'media/test.png')
    
