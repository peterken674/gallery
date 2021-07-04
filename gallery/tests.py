from django.test import TestCase
from .models import Image, Location, Category

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

        