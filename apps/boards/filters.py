import django_filters
from django.db.models import Q

from apps.boards.models import Board


class BoardFilter(django_filters.FilterSet):
    keyword = django_filters.Filter(method="filter_keyword")

    def filter_keyword(self, queryset, name, value):
        return queryset.filter(Q(title__icontains=value) | Q(content__icontains=value))

    class Meta:
        model = Board
        fields = ["keyword"]
