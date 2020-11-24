import django_filters
from django_filters import DateFilter, CharFilter, TimeFilter, ChoiceFilter, MultipleChoiceFilter, NumberFilter
from .models import AndroidApp

class AppFilter(django_filters.FilterSet):
    print("in link filter")
    handle = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = AndroidApp
        fields = {
        'sha256':['iexact'],
        }
