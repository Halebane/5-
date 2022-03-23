import django_filters

import core.models


class BookFilter(django_filters.FilterSet):
    name = django_filters.Filter(lookup_expr='icontains')
    class Meta:
        model = core.models.Book
        fields = '__all__'
