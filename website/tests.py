from django.http import response
from django.test import TestCase, SimpleTestCase

# Create your tests here.
class simpletests(SimpleTestCase):
    def test_website_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)