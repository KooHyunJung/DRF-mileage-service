from django.urls import path

from mileage.views import hello_world_drf

urlpatterns = [
    path('hello_world_drf/', hello_world_drf),
    # path('post/events/', EventReviewMileage.as_view()),

]
