from django.db.models import QuerySet
from django.db.models import F

from .filters import SearchFilter


def sort_products_by_price(products: QuerySet, sort_by: str) -> QuerySet:
    """ Сортирует товары по цене """
    if sort_by == "l2h":
        return products.order_by(F('price') - (F('price') * F('sale') / 100))
    elif sort_by == "h2l":
        return products.order_by(-(F('price') - (F('price') * F('sale') / 100)))
    else:
        return products


def search_products_by_form(products: QuerySet, search_query: str) -> QuerySet:
    """ Ищет товар по запросу из формы """
    if search_query is not None:
        return SearchFilter.form_search_filter(products, search_query)
    else:
        return products
