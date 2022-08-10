
import uuid
from django.db import models
from datetime import datetime
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):

    REQUIRED_FIELDS = ('email_address',)
    USERNAME_FIELD = "uuid"

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.TextField(null=False, blank=True)
    last_name = models.TextField(null=False, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    email_address = models.TextField(null=False, blank=False, unique=True)
    user_password = models.TextField(null=False)
    is_active = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        pass


    def __str__(self):
        return f"{self.full_name} | {self.email_address}"
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False
    
    @property
    def is_authenticated(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return True
