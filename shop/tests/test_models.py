from django.test import TestCase
from shop.models import Product, Purchase
from datetime import datetime


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="chair", price="15000")
        Product.objects.create(name="sofa", price="35000")

    def test_correctness_types(self):
        self.assertIsInstance(Product.objects.get(name="chair").name, str)
        self.assertIsInstance(Product.objects.get(name="chair").price, int)
        self.assertIsInstance(Product.objects.get(name="sofa").name, str)
        self.assertIsInstance(Product.objects.get(name="sofa").price, int)

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="chair").price == 15000)
        self.assertTrue(Product.objects.get(name="sofa").price == 35000)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_chair = Product.objects.create(name="chair", price="15000")
        self.datetime = datetime.now()
        Purchase.objects.create(product=self.product_chair,
                                person="Ivanov",
                                address="Svetlaya St.")

    def test_correctness_types(self):
        self.assertIsInstance(
            Purchase.objects.get(product=self.product_chair).person, str)
        self.assertIsInstance(
            Purchase.objects.get(product=self.product_chair).address, str)
        self.assertIsInstance(
            Purchase.objects.get(product=self.product_chair).date, datetime)

    def test_correctness_data(self):
        self.assertTrue(
            Purchase.objects.get(product=self.product_chair).person == "Ivanov")
        self.assertTrue(
            Purchase.objects.get(product=self.product_chair).address
            == "Svetlaya St.")
        self.assertTrue(
            Purchase.objects.get(product=self.product_chair)
            .date.replace(microsecond=0) ==
            self.datetime.replace(microsecond=0))
