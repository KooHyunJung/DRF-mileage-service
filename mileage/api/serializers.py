from rest_framework import serializers

from mileage.models.point import Point
from mileage.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "user_id", "place_id", "content", "photo_id")


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ("user_id", "total")
