from django.test import TestCase

from django.test import TestCase
from .models import Post,  Profile, Location, NeighbourHood, Business
from django.contrib.auth.models import User

# Create your tests here.

# Neighbourhood Model Tests
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        # create a location instance
        self.location = Location(name='Test Location')
        self.location.save_location()
        # create an admin user
        self.admin = User.objects.create_superuser(
            username='developer',
            password='password'
        )
        self.neighbourhood = NeighbourHood(
            name='Test Neighbourhood', location=self.location, occupants_count=100, admin_id=self.admin.id)
    
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood, NeighbourHood))

    def test_save_method(self):
        self.neighbourhood.create_neigborhood()
        neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhoods) > 0)

    def test_delete_method(self):
        self.neighbourhood.create_neigborhood()
        self.neighbourhood.delete()
        neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhoods) == 0)

