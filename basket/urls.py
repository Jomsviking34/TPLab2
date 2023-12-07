from . import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^$', views.basket_detail, name='basket_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$',
            views.basket_add, name='basket_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$',
            views.basket_remove, name='basket_remove'),
]
