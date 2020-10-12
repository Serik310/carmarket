import django_filters
from .models import Car, CarType

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        fields = ['carTitle','engine','transmission']