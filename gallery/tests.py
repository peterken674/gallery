from django.test import TestCase
from .models import Image, Location
from .models import Category

class LocationTest(TestCase):
    def setUp(self) -> None:
        self.test_location = Location(name='Nairobi', country='Kenya')

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
        self.assertEqual(Location.objects.filter(name='Nairobi').first().country, 'Kenya')
        self.assertTrue(len(Location.objects.all()) == 1)
        self.test_location.update_location('Kigali', 'Rwanda')
        self.assertEqual(Location.objects.filter(name='Kigali')[0].country, 'Rwanda')

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
        self.assertEqual(Category.objects.get(name='pets').name, 'pets')
        self.assertTrue(len(Category.objects.all()) == 1)
        self.test_category.update_category('travel')
        self.assertTrue(len(Category.objects.all()) == 1)
        self.assertEqual(Category.objects.all().first().name, 'travel')
