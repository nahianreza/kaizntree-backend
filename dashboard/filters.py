import django_filters 
from .models import Item

class ItemFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    category = django_filters.CharFilter(field_name="category__name", lookup_expr='iexact')
    tags = django_filters.AllValuesMultipleFilter(field_name="tags__name")
    in_stock = django_filters.BooleanFilter(field_name="in_stock")

    class Meta:
        model = Item
        fields = ['in_stock', 'category', 'tags', 'start_date', 'end_date']