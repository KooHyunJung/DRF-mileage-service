from rest_framework import serializers

from mileage.models.event import Event
from mileage.models.point import Point
from mileage.models.review import Review


class EventSerializer(serializers.ModelSerializer):
    attachedPhotoIds = serializers.ListField(required=False)

    class Meta:
        model = Event
        fields = (
            "type",
            "action",
            "reviewId",
            "content",
            "attachedPhotoIds",
            "userId",
            "placeId",
        )


class ReviewSerializer(serializers.ModelSerializer):
    photo_id = serializers.ListField(required=False)

    class Meta:
        model = Review
        fields = ("id", "user_id", "place_id", "content", "photo_id")


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ("user_id", "point_total")
