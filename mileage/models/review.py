import uuid

from django.db import models


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    place_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=True)
    content = models.TextField()
    photo_id = models.TextField(blank=True)
    # photo_id -> uuid list 전체 저장. json 인코딩 디코딩 사용 예정
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
