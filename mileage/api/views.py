from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mileage.api.serializers import PointSerializer
from mileage.api.services.add_service import creat_review_and_point_count
from mileage.api.services.delete_survice import delete_review_and_point_count
from mileage.api.services.mod_survice import update_review_and_point_count

from mileage.models import Point, Review


@api_view(["POST"])
def event_api(request):
    # create
    if request.data["action"] == "ADD":
        user_id = request.data["userId"]
        place_id = request.data["placeId"]

        """
        리뷰 작성 중복 확인
        DB 쿼리 날려서 확인 인스턴스 있으면 error, 없으면 create 진행
        """

        if Review.objects.get(user_id=user_id, place_id=place_id):
            # DB에 쿼리를 보냈을 때 인스턴스 반환
            try:
                Response({"msg": "이미 작성한 장소입니다."}, status=status.HTTP_400_BAD_REQUEST)
            # DoesNotExist 발생 - create 진행
            except Review.DoesNotExist:
                creat_event = creat_review_and_point_count(request)
                return Response(creat_event.data, status=status.HTTP_201_CREATED)

    # update
    elif request.data["action"] == "MOD":
        user_id = request.data["userId"]
        review_id = request.data["reviewId"]

        """
        리뷰 작성자 본인 확인 후 update 진행
        user 모델 사용시 => if request.user.id == user_id 
        """

        if Review.objects.get(id=review_id, user_id=user_id):
            # 본인 인증 완료 update 진행
            try:
                update_event = update_review_and_point_count(request)
                return Response(update_event.data, status=status.HTTP_200_OK)
            # 본인 인증 실패 or 해당 리뷰 없음
            except Review.DoesNotExist:
                return Response({"msg": "본인 수정만 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)

    # delete
    elif request.data["action"] == "DELETE":
        user_id = request.data["userId"]
        review_id = request.data["reviewId"]

        """
        리뷰 작성자 본인 확인 후 delete 진행
        user 모델 사용시 => if request.user.id == user_id 
        """

        if Review.objects.get(id=review_id, user_id=user_id):
            # 본인 인증 완료 delete 진행
            try:
                delete = delete_review_and_point_count(request)
                return Response({"msg": delete})
            # 본인 인증 실패 or 해당 리뷰 없음
            except Review.DoesNotExist:
                return Response({"msg": "작성자 본인만 삭제 가능합니다."}, status=status.HTTP_400_BAD_REQUEST)


# user point 조회 api
class PointMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    lookup_field = "user_id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
