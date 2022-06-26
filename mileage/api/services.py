# views.py 서비스 함수
from mileage.api.serializers import ReviewSerializer
from mileage.models import Review


def creat_review_and_point_count(request):
    creat_event = ReviewSerializer(data=request.data)
    if creat_event.is_valid():
        creat_event.user_id = request.data["user_id"]
        creat_event.place_id = request.data["place_id"]
        creat_event.content = request.data["content"]
        creat_event.save()
    return creat_event


def update_review_and_point_count(request):
    update_event = ReviewSerializer(data=request.data)
    if update_event.is_valid():
        update_event.user_id = request.data["user_id"]
        update_event.place_id = request.data["place_id"]
        update_event.content = request.data["content"]
        update_event.save()
    return update_event


def delete_review_and_point_count(request):
    delete_event = Review.objects.get(id=request.data["user_id"])
    delete_event.delete()
    return "delete"
