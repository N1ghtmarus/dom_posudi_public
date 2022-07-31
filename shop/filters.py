import django_filters
from django.db.models import Q

from .models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['price']


class SearchFilter(django_filters.FilterSet):
    """ Фильтр находит запрошенные продукты из queryset """
    queryset = django_filters.CharFilter(method='search_filter', label="Search")

    class Meta:
        model = Product
        fields = ['queryset']

    def form_search_filter(queryset, search_query):
        return queryset.filter(
            Q(description__contains=search_query) |
            Q(name__contains=search_query) |
            Q(category__name__contains=search_query) |
            Q(maker__company__contains=search_query) |
            Q(SKU__contains=search_query)
        )


# advanced search, but not working because of sqlite3 features I think
    # def form_search_filter(queryset, search_query):
    #     query = SearchQuery(queryset)
    #     name_vector = SearchVector('name')
    #     description_vector = SearchVector('description')
    #     vectors = name_vector + description_vector
    #     qs = queryset.annotate(search=vectors,).filter(search=search_query)
    #     return qs
