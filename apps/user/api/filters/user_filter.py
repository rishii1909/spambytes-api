from django_filters import rest_framework as filters
from django.db.models.functions import Concat
from django.db.models import Value as V

from apps.user.models import User


class UserFilter(filters.FilterSet):

    uuid = filters.UUIDFilter(field_name='uuid', lookup_expr='exact')

    created_lte = filters.DateFilter(field_name='created__date', lookup_expr='lte')
    created_gte = filters.DateFilter(field_name='created__date', lookup_expr='gte')

    user_name = filters.CharFilter(method='user_full_name')
    user_phone = filters.CharFilter(field_name='phone_number', lookup_expr='icontains')
    user_email = filters.CharFilter(field_name='email_address', lookup_expr='icontains')


    class Meta:
        model = User
        fields = {
            'uuid': ['exact'],
            'email_address': ['exact']
        }

    def user_full_name(self, queryset, name, value):
        return queryset.annotate(fullname=Concat('first_name', V(' '), 'last_name')).filter(fullname__icontains=value)
