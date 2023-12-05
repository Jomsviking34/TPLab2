from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from basket.forms import BasketAddProductForm
from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    basket_product_form = BasketAddProductForm()
    context = {'products': products,'basket_product_form': basket_product_form}
    return render(request, 'shop/index.html', context)
   # return render(request, 'shop/index.html', ['products': products])


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')

def about(request):
    context = {}
    return render(request, 'shop/about.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    basket_product_form = BasketAddProductForm()
    context = {'product': product,'basket_product_form': basket_product_form}
    return render(request, 'shop/product/detail.html', context)