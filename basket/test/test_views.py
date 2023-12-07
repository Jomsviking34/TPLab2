from django.test import TestCase, Client
from shop.views import PurchaseCreate


# Create your tests here.

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    # Досягаемость страниц
    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)