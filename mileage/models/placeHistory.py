import uuid

from django.db import models


class PlaceHistory(models.Model):
    place_id = models.UUIDField(default=uuid.uuid4(), editable=True)
    review_total = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
