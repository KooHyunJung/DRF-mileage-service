# views.py 서비스 함수
import json

from mileage.api.serializers import EventSerializer
from mileage.models import Review


def creat_review_and_point_count(request):
    # 생성 완료 + 포인트 진행 중
    creat_event = EventSerializer(data=request.data)
    if creat_event.is_valid():
        creat_event.type = request.data["type"]
        creat_event.action = request.data["action"]
        creat_event.reviewId = request.data["reviewId"]
        creat_event.content = request.data["content"]
        creat_event.attachedPhotoIds = json.dumps(request.data["attachedPhotoIds"])
        creat_event.userId = request.data["userId"]
        creat_event.placeId = request.data["placeId"]
        creat_event.save()
    return creat_event


def update_review_and_point_count(request):
    # 수정 진행 중 + 포인트 진행 중
    update_event = EventSerializer(data=request.data)
    if update_event.is_valid():
        update_event.user_id = request.data["userId"]
        update_event.place_id = request.data["placeId"]
        update_event.content = request.data["content"]
        update_event.save()
    return update_event


def delete_review_and_point_count(request):
    # 석제 완료 + 포인트 진행 중
    delete_event = Review.objects.get(id=request.data["user_id"])
    delete_event.delete()
    return "delete"
