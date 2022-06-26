from django.db import models

from mileage.models.place import Place


class PlaceHistory(models.Model):
    place_id = models.OneToOneField(
        Place, on_delete=models.CASCADE, db_column="place_id"
    )
    status = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
