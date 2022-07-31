from django.urls import path

from .views import (
                    ProductAPIList,
                    ProductAPICRUD,
                    OrderAPIList,
                    OrderAPICRUD,
                    CategoryAPIList,
                    CategoryAPICRUD,
                    OrderItemAPIList,
                    OrderItemAPICRUD
                    )


app_name = 'api_v1'


urlpatterns = [
    path('product_list/', ProductAPIList.as_view()),
    path('product_list/<int:pk>/', ProductAPICRUD.as_view()),
    path('category_list/', CategoryAPIList.as_view()),
    path('category_list/<int:pk>/', CategoryAPICRUD.as_view()),
    path('order_list/', OrderAPIList.as_view()),
    path('order_list/<int:pk>/', OrderAPICRUD.as_view()),
    path('order_item_list/', OrderItemAPIList.as_view()),
    path('order_item_list/<int:pk>/', OrderItemAPICRUD.as_view()),
]
