from django.contrib.auth.models import User
from django.db import models


class Point(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
