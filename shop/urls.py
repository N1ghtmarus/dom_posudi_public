from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.ListProduct.as_view(), name='product_list'),
    path(
        'products/<slug:category_slug>/',
        views.ListProduct.as_view(),
        name='product_list_by_category'
        ),

    path('on_sale/', views.ListSale.as_view(), name='product_list_sale'),
    path(
        'on_sale/<slug:category_slug>/',
        views.ListSale.as_view(),
        name='product_list_sale_by_category'
        ),

    path(
        '<int:id>/<slug:slug>/',
        views.ShowProduct.as_view(),
        name='product_detail'
        ),
    path('shop_address/', views.ShopAdress.as_view(), name='shop_address'),
]
