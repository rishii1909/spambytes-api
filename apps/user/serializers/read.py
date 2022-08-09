import logging
from rest_framework import serializers
from rest_framework.fields import UUIDField

from apps.user.models import User


class GetUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "uuid",
            "first_name",
            "last_name",
            "email_address",
            "phone_number",
            "is_active"
        ]