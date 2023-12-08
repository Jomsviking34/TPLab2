from django.test import TestCase, Client, RequestFactory
from shop.views import PurchaseCreate
from shop.models import Product

# Create your tests here.


class ViewTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="chair", price="15000")
        Product.objects.create(name="sofa", price="35000")
        self.client = Client()
        self.factory = RequestFactory()

    # Досягаемость страниц
    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)

    # Запросы на добавление и удаление
    def test_view_posts(self):
        response = self.client.get('/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/basket/add/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/basket/')
        response = self.client.post('/basket/remove/1/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/basket/')