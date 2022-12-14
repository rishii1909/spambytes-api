from datetime import date
from drf_rw_serializers.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from django_filters.rest_framework import DjangoFilterBackend
from apps.user.api.filters.user_filter import UserFilter
from apps.user.constants.user_constants import DELETE_SUCCESS

from apps.user.models import User
from apps.user.serializers.create import CreateUserSerializer
from apps.user.serializers.read import GetUserSerializer


class UserListCreateAPI(ListCreateAPIView):
    """
    User Objects GET and POST API
    """
    queryset = User.objects.filter(deleted=False)
    read_serializer_class = GetUserSerializer
    write_serializer_class = CreateUserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = UserFilter

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.pk
        return self.create(request, *args, **kwargs)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.filter(deleted=False)
    read_serializer_class = GetUserSerializer
    write_serializer_class = CreateUserSerializer
    lookup_field = 'uuid'

    @swagger_auto_schema(request_body=CreateUserSerializer)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=CreateUserSerializer)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        request.data['deleted_on'] = date.today()
        self.patch(request, *args, **kwargs)
        self.destroy(request, *args, **kwargs)
        return DELETE_SUCCESS