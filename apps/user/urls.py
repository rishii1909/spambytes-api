from django.urls import path, include, re_path
from rest_framework import routers

from apps.user.api.crud_api import UserDetailView, UserListCreateAPI


urlpatterns = (
    path("user/", UserListCreateAPI.as_view()),
    path("user/<uuid>/", UserDetailView.as_view())
)
