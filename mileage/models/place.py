import uuid

from django.db import models


class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=True)
    name = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=256, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
