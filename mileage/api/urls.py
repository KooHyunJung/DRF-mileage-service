from django.urls import path

from mileage.api.views import EventGeneric, PointMixins

urlpatterns = [
    path("events", EventGeneric.as_view()),
    path("points/<int:user_id>", PointMixins.as_view())
    # path("post/events/<int:pk>", EventViewSet.as_view({'get': 'MOD'})),
    # path("post/events/<int:pk>", EventViewSet.as_view({'get': 'DELETE'})),
]
