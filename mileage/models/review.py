from django.contrib.auth.models import User
from django.db import models

from mileage.models.place import Place


class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE, db_column="place_id")
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
