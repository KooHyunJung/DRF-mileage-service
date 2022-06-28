from django.db import models

from mileage.models.point import Point
from mileage.models.review import Review


class PointHistory(models.Model):
    point_id = models.ForeignKey(Point, on_delete=models.CASCADE, db_column="point_id")
    review_id = models.ForeignKey(
        Review, on_delete=models.CASCADE, db_column="review_id"
    )
    content_point = models.IntegerField(default=0)
    photo_point = models.IntegerField(default=0)
    start_point = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
