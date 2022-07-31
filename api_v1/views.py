from shop.models import Product, Category
from orders.models import Order, OrderItem

from .serializers import (
                        ProductSerializer,
                        OrderSerializer,
                        CategorySerializer,
                        OrderItemSerializer
                        )
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAdminUser
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics


class APIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


# ProductAPI
class ProductAPIList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = APIListPagination


class ProductAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


# CategoryAPI
class CategoryAPIList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = APIListPagination


class CategoryAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)


# OrderAPI
class OrderAPIList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAdminUser,)


class OrderAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)


# OrderItemAPI
class OrderItemAPIList(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAdminUser,)


class OrderItemAPICRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAdminUser,)
