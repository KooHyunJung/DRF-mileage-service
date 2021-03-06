import uuid

from django.db import models


class Point(models.Model):
    user_id = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=True)
    point_total = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
