import uuid

from django.db import models


class PointHistory(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4(), editable=True)
    place_id = models.UUIDField(default=uuid.uuid4(), editable=True)
    review_id = models.UUIDField(default=uuid.uuid4(), editable=True)
    content_point = models.IntegerField(default=0)
    photo_point = models.IntegerField(default=0)
    start_point = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
