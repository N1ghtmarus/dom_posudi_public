from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.db.models import QuerySet
import logging

from .models import Category, Product
from .filters import ProductFilter
from cart.forms import CartAddProductForm
from .product_search import sort_products_by_price, search_products_by_form


logger = logging.getLogger(__name__)


class ListProduct(ListView):
    """ Веб-сервис, позволяющий получить товары сайта,
    отсортироать их и найти нужные товары по имени"""
    model = Product
    template_name = 'shop/product/list.html'
    slug_url_kwarg = 'category_slug'
    paginate_by = 9

    category = None
    product_cat = None
    categories = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _get_context(self, context, only_on_sale=False)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        output_queryset = _get_output_queryset(
                                                self,
                                                queryset,
                                                only_on_sale=False
                                                )
        return ProductFilter(self.request.GET, output_queryset).qs


class ListSale(ListView):
    """ Веб-сервис, позволяющий получить скидочные товары сайта,
    отсортироать их и найти нужные товары по имени"""
    model = Product
    template_name = 'shop/product/sales_list.html'
    slug_url_kwarg = 'category_slug'
    paginate_by = 9

    category = None
    product_cat = None
    categories = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        _get_context(self, context, only_on_sale=True)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        output_queryset = _get_output_queryset(
                                                self,
                                                queryset,
                                                only_on_sale=True
                                                )
        return ProductFilter(self.request.GET, output_queryset).qs


def _get_context(self, context: dict, only_on_sale: bool) -> dict:
    """ Определяет и отдает значения словоря context """
    context['products'] = self.model
    context['category'] = self.category
    context['categories'] = self.categories
    context['product_cat'] = self.product_cat
    category_slug = self.kwargs.get('category_slug')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        if only_on_sale:
            filter_product = Product.objects.filter(
                                                    category=category,
                                                    available=True,
                                                    on_sale=True
                                                    )
        else:
            filter_product = Product.objects.filter(
                                                    category=category,
                                                    available=True
                                                    )
        product_cat = filter_product.count()
        context['category'] = category
        context['product_cat'] = product_cat
    return context


def _get_output_queryset(self, queryset: QuerySet, only_on_sale: bool) -> QuerySet:
    """ Применяет пользовательсие фильтры к запросу и отдает Queryset """
    sort_by = self.request.GET.get("price_sort")
    category_slug = self.kwargs.get('category_slug')
    search = self.request.GET.get('search')
    if only_on_sale:
        on_sale = [True]
    else:
        on_sale = [True, False]
    if category_slug:
        products = Product.objects.filter(
                                        category__slug=category_slug,
                                        available=True,
                                        on_sale__in=on_sale
                                        )
        queryset = search_products_by_form(sort_products_by_price(products, sort_by), search)
        return queryset
    products = Product.objects.filter(available=True, on_sale__in=on_sale)
    queryset = search_products_by_form(sort_products_by_price(products, sort_by), search)
    return queryset


class ShowProduct(DetailView):
    """ View-класс конкретного товара, позваляющий =
    выбрать его кол-во и положить в корзину """
    model = Product
    template_name = 'shop/product/detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['cart_product_form'] = cart_product_form
        return context


class ShopAdress(TemplateView):
    """ View-класс страницы адреса магазина"""
    template_name = 'shop/address/shop_address.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
