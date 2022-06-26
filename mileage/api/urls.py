from django.urls import path

from mileage.api.views import event_api, PointMixins

urlpatterns = [
    path("events", event_api),
    path("points/<int:user_id>", PointMixins.as_view())
]
