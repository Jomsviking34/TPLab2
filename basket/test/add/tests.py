from django.test import TestCase, Client
from shop.models import Product
from basket.basket import Basket
# Create your tests here.

class BasketTestCaseAdd(TestCase):
    def setUp(self):
        Product.objects.create(name='sofa 3',price=35000)
        Product.objects.create(name='sofa 4',price=45000)
        self.client = Client()
    # Добавление товара
    def test_basket_add(self):
        response = self.client.get('/basket/')
        session = self.client.session
        basket = Basket(self.client)
        basket.add(Product.objects.get(id = 1))
        self.assertEqual(basket.basket['1']['quantity'], 1)
        basket.add(Product.objects.get(id = 1))
        self.assertEqual(basket.basket['1']['quantity'], 2)