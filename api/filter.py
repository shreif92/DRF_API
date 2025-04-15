from django_filters.rest_framework import FilterSet
from .models import *


class BooksFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'category':['exact'],
            'author':['icontains']
            }