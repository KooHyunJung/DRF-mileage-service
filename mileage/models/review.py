import uuid

from django.db import models

from mileage.models.place import Place
from mileage.models.user import UserModel


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    user_id = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, db_column="user_id"
    )
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, db_column="place_id")
    content = models.TextField()
    photo_id = models.TextField(blank=True)
    # photo_id -> uuid list 전체 저장. json 인코딩 디코딩 사용 예정
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
