from django.test import TestCase, Client
from shop.models import Product
from basket.basket import Basket


# Create your tests here.

class BasketTestCaseRemove(TestCase):
    def setUp(self):
        Product.objects.create(name='sofa 3', price=35000)
        Product.objects.create(name='sofa 4', price=45000)
        self.client = Client()

    # Удаление товара
    def test_basket_remove(self):
        response = self.client.get('/basket/')
        session = self.client.session
        basket = Basket(self.client)
        basket.add(Product.objects.get(id=1))
        basket.remove(Product.objects.get(id=1))
        self.assertEqual(len(basket.basket), 0)
