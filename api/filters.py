from django_filters import rest_framework as filters

from .models import *


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(
        field_name='genre__slug',
    )
    category = filters.CharFilter(
        field_name='category__slug',
    )
    name = filters.CharFilter(
        lookup_expr="contains",
    )

    class Meta:
        model = Title
        fields = [
            'genre',
            'category',
            'name',
            'year',
        ]