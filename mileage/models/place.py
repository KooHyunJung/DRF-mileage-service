from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
