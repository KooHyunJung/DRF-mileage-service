# views.py create 서비스 함수
from mileage.api.serializers import EventSerializer, ReviewSerializer
from mileage.models import PlaceHistory, Point, PointHistory


def creat_review_and_point_count(request):
    user_id = request.data["userId"]
    place_id = request.data["placeId"]
    review_id = request.data["reviewId"]
    content = request.data["content"]
    photo_id = request.data["attachedPhotoIds"]
    cont = 0
    photo = 0
    start = 0

    # 포인트 점수 계산
    if content is not None:
        cont += 1
    else:
        cont += 0
    if photo_id is not None:
        photo += 1
    else:
        photo += 0
    if PlaceHistory.objects.get(place_id=place_id).review_total == 0:
        start += 1
    else:
        start += 0

    # request.data Event 모델에 저장
    creat_event = EventSerializer(data=request.data)
    if creat_event.is_valid():
        creat_event.save()

    # request.data Review 모델에 저장
    creat_review = ReviewSerializer(data=request.data)
    if creat_review.is_valid():
        creat_review.id = request.data["reviewId"]
        creat_review.user_id = request.data["userId"]
        creat_review.place_id = request.data["placeId"]
        creat_review.content = request.data["content"]
        creat_review.photo_id = request.data["attachedPhotoIds"]
        creat_review.save()

    # Point 모델 없다면 생성
    if Point.objects.create(user_id=user_id):
        try:
            pass
        except Point.DoesNotExist:
            Point.objects.create(user_id=user_id)

    # PointHistory 데이터 저장
    point_id = Point.objects.get(user_id=user_id).id
    PointHistory.objects.create(
        point_id=Point.objects.get(id=point_id),
        review_id=Point.objects.get(id=review_id),
        content_point=content,
        photo_point=photo,
        start_point=start,
    )

    # Point 데이터 저장 : point_total
    point_total = Point.objects.get(point_id=point_id).point_total
    point_sum = int(point_total) + content + photo + start
    Point.objects.filter(user_id=user_id).update(point_total=point_sum)

    return creat_event


