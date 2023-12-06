from django.test import TestCase, Client
from shop.views import PurchaseCreate
from shop.models import Product
from selenium import webdriver
# Create your tests here.

class ViewTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='sofa 1',price=35000)
        Product.objects.create(name='sofa 2',price=40000)
        self.client = Client()
    # Досягаемость страниц
    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/3/')
        self.assertEqual(response.status_code, 404)