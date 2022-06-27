import uuid

from django.db import models


class Event(models.Model):
    type = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=True)
    action = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=True)
    reviewId = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=True)
    content = models.TextField()
    attachedPhotoIds = models.TextField(blank=True)
    # photo_id -> uuid list 전체 저장. json 인코딩 디코딩 사용 예정
    userId = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=True)
    placeId = models.UUIDField(primary_key=False, default=uuid.uuid4(), editable=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

