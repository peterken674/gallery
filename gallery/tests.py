from django.test import TestCase
from .models import Image, Location
from .models import Category

class LocationTest(TestCase):
    def setUp(self):
        self.test_location = Location(name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_location, Location))

    def test_save_location(self):
        self.test_location.save_location()
        self.assertTrue(len(Location.objects.all()) > 0)

    def test_delete_location(self):
        self.test_location.save_location()
        self.assertTrue(len(Location.objects.all()) > 0)
        self.test_location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)

    def test_update_location(self):
        self.test_location.save_location()
        self.test_location.update_location(self.test_location.id, 'Nyeri')
        self.assertTrue(Location.objects.get(name='Nyeri').name, 'Nyeri')
        self.assertTrue(len(Location.objects.all())==1)

class CategoryTest(TestCase):
    def setUp(self):
        self.test_category = Category(name='pets')

    def test_instance(self):
        self.assertTrue(isinstance(self.test_category, Category))

    def test_save_category(self):
        self.test_category.save_category()   
        self.assertTrue(len(Category.objects.all()) > 0)

    def test_delete_category(self):     
        self.test_category.save_category()
        self.assertTrue(len(Category.objects.all()) > 0)
        self.test_category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)

    def test_update_category(self):
        self.test_category.save_category()
        self.test_category.update_category(self.test_category.id, 'travel')
        self.assertTrue(Category.objects.get(name='travel').name, 'travel')
        self.assertTrue(len(Category.objects.all())==1)

class ImageTest(TestCase):
    '''Class to test the Image class.
    '''

    def setUp(self):
        self.mombasa = Location(name='Mombasa')
        self.mombasa.save_location()

        self.travel = Category(name='travel')
        self.travel.save_category()

        self.cruising_image=Image(name='Cruise',description='Crusising along the coast of Mombasa',location=self.mombasa,category=self.travel)

    def test_instance(self):
        self.assertTrue(isinstance(self.cruising_image, Image))

    def test_save_image(self):
        self.cruising_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)

    def test_delete_image(self):     
        self.cruising_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)
        self.cruising_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update_image(self):
        self.cruising_image.save_image()
        self.cruising_image.update_image(self.cruising_image.id,image='media/test.png')
        self.assertEqual(Image.objects.get(image='media/test.png').image,'media/test.png')
    
    def test_get_image_by_id(self):
        self.cruising_image.save_image()
        self.assertTrue(len(Image.get_image_by_id(self.cruising_image.id))>0)

    def test_filter_by_location(self):
        self.cruising_image.save_image()
        self.assertTrue(len(Image.filter_by_location(self.mombasa)) == 1)

    def test_search_image(self):
        self.cruising_image.save_image()
        self.assertTrue(len(Image.search_image(self.travel)) == 1)
