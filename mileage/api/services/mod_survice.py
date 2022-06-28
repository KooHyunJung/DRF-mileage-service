# views.py update 서비스 함수
from mileage.api.serializers import EventSerializer, ReviewSerializer
from mileage.models import Event, Point, PointHistory, Review


def update_review_and_point_count(request):
    user_id = request.data["userId"]
    place_id = request.data["placeId"]
    review_id = request.data["reviewId"]
    content = request.data["content"]
    photo_id = request.data["attachedPhotoIds"]
    cont = 0
    photo = 0
    start_point = PointHistory.objects.get(review_id=review_id).start_point

    # 기존 점수 update 데이터 비교 계산
    content_point = PointHistory.objects.get(review_id=review_id).content_point
    photo_point = PointHistory.objects.get(review_id=review_id).photo_point

    if (content is not None) and (content_point == 1):
        cont += 0
    elif (content is not None) and (content_point == 0):
        cont += 1
    else:
        cont += 0

    if (photo_id is not None) and (photo_point == 1):
        photo += 0
    elif (photo_id is not None) and (photo_point == 0):
        photo += 1
    else:
        photo += 0

    # request.data Event 모델에 저장
    update_event = EventSerializer(data=request.data)
    if update_event.is_valid():
        update_event.save()

    # Review 모델 데이터 update
    update_id = Review.objects.get(id=user_id)
    update_review = ReviewSerializer(update_id)
    if update_review.is_valid():
        update_review.id = review_id
        update_review.user_id = user_id
        update_review.place_id = place_id
        update_review.content = content
        update_review.photo_id = photo_id
        update_review.save()

    # PointHistory 데이터 update
    point_id = Point.objects.get(user_id=user_id).id
    PointHistory.objects.filter(
        point_id=Point.objects.get(id=point_id),
        review_id=Point.objects.get(id=review_id)
    ).update(
        content_point=content,
        photo_point=photo,
        start_point=start_point,
    )

    # Point 데이터 저장 : point_total
    point_total = Point.objects.get(point_id=point_id).point_total
    point_sum = int(point_total) + content + photo + int(start_point)
    Point.objects.filter(user_id=user_id).update(point_total=point_sum)

    return update_event


