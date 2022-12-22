import django_filters
from django_filters import FilterSet
from .models import Post
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class PostFilter(FilterSet):
    header = django_filters.CharFilter(lookup_expr='icontains')
    author__username = django_filters.CharFilter(lookup_expr='icontains')
    date = django_filters.DateFilter(
        widget=DateInput(
            attrs={
                'class': 'datepicker'
            }
        )
    )

    class Meta:
        model = Post
        fields = ['header', 'date', 'author__username']
