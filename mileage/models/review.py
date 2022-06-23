from django.contrib.auth.models import User
from django.db import models

from mileage.models.place import Place


class Review(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    placeId = models.ForeignKey(Place, on_delete=models.CASCADE)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
