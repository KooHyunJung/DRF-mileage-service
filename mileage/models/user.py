import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# User 모델 커스텀
class UserModel(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
