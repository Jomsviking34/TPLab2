from django.test import TestCase, Client
from shop.models import Product
from basket.basket import Basket


# Create your tests here.

class BasketTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    # Добавление товара
    def test_basket_add(self):
        response = self.client.get('/basket/')
        session = self.client.session
        basket = Basket(self.client)
        product1 = Product(id = 1,name='sofa 3', price=35000)
        basket.add(product1)
        self.assertEqual(basket.basket['1']['quantity'], 1)
        basket.add(product1)
        self.assertEqual(basket.basket['1']['quantity'], 2)

    def test_basket_remove(self):
        response = self.client.get('/basket/')
        session = self.client.session
        basket = Basket(self.client)
        product1 = Product(id = 1,name='sofa 3', price=35000)
        basket.add(product1)
        self.assertEqual(basket.basket['1']['quantity'], 1)
        basket.remove(product1)
        self.assertEqual(len(basket.basket), 0)

    def test_basket_total(self):
        response = self.client.get('/basket/')
        session = self.client.session
        basket = Basket(self.client)
        product1 = Product(id = 1,name='sofa 3', price=35000)
        basket.add(product1)
        self.assertEqual(basket.get_total_price(), 35000)
        basket.add(product1)
        self.assertEqual(basket.get_total_price(), 70000)