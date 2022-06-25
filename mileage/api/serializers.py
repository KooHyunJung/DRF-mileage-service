from rest_framework import serializers

from mileage.models.point import Point
from mileage.models.review import Review
from mileage.models.reviewPhoto import ReviewPhoto


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("user_id", "place_id", "content")


class ReviewPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewPhoto
        fields = ("review_id", "url")


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ("user_id", "total", "updated_at", "created_at")
