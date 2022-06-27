from rest_framework import serializers

from mileage.models.point import Point
from mileage.models.event import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ("type", "action", "reviewId", "content", "attachedPhotoIds", "userId", "placeId")


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ("user_id", "point_total")
