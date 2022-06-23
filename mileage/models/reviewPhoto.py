from django.db import models

from mileage.models.review import Review


class ReviewPhoto(models.Model):
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    url = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
