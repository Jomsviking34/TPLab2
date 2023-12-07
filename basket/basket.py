from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Basket(object):

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            # сохранение пустой корзины в сессии
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    # Добавление товара
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        # Если товара ещё нет в корзине
        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': 0,
                                       'price': str(product.price)}
        # Если задан флаг обновления кол-ва
        if update_quantity:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id]['quantity'] += quantity
        # Сохранить сессию
        self.save()

    # Сохранение сессии
    def save(self):
        # Обновление сессии
        self.session[settings.BASKET_SESSION_ID] = self.basket
        # Отметка сессии как изменённой
        self.session.modified = True

    # Удаление товара
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    # Перебор товаров
    def __iter__(self):
        product_ids = self.basket.keys()
        # Получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.basket[str(product.id)]['product'] = product

        for item in self.basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # Получение общего кол-ва товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    # Получение общей цены
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.basket.values())

    # Очистка сеанса корзины
    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.session.modified = True
