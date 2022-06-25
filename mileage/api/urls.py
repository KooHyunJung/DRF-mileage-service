from django.urls import path

from mileage.api.views import EventAPIView, PointMixins

urlpatterns = [
    path("events", EventAPIView.as_view()),
    path("points/<int:user_id>", PointMixins.as_view())
]
