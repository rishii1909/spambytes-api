
import uuid
from django.db import models
from datetime import datetime
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class User(TimeStampedModel):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    first_name = models.TextField(null=False, blank=True)
    last_name = models.TextField(null=False, blank=True)
    phone_number = models.TextField(null=True, blank=True, unique=True)
    email_address = models.TextField(null=True, blank=True)
    user_password = models.TextField()
    is_active = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} | {self.email_address}"
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name