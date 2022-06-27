from django.db import models

from mileage.models.user import UserModel


# 개인 1:1
class Point(models.Model):
    user_id = models.OneToOneField(
        UserModel, on_delete=models.CASCADE, primary_key=True, db_column="user_id"
    )
    total = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
