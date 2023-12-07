from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('buy/<int:product_id>/', views.PurchaseCreate.as_view(), name='buy'),
    re_path(r'^(?P<id>\d+)/$', views.product_detail, name='product_detail')
]
