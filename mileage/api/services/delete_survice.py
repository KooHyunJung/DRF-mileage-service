# views.py delete 서비스 함수
from mileage.models import Review, PointHistory, Point


def delete_review_and_point_count(request):
    review_id = request.data["reviewId"]
    user_id = request.data["user_id"]

    # point 계산
    content_point = PointHistory.objects.get(review_id=review_id).content_point
    photo_point = PointHistory.objects.get(review_id=review_id).photo_point
    start_point = PointHistory.objects.get(review_id=review_id).start_point

    point = Point.objects.get(user_id=user_id).point_total
    point_sum = int(content_point) + int(photo_point) + int(start_point)

    point_result = int(point) - int(point_sum)

    Point.objects.filter(user_id=user_id).update(point_total=point_result)

    # 해당 데이터 삭제
    delete_event = Review.objects.get(id=user_id)
    delete_event.delete()
    return "삭제 완료"
