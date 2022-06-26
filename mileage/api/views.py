from rest_framework import generics, mixins, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mileage.api.serializers import PointSerializer
from mileage.api.services import (
    creat_review_and_point_count,
    update_review_and_point_count,
    delete_review_and_point_count
)

from mileage.models import Point


@api_view(['POST'])
def event_api(request):
    # creat
    if request.data['action'] == "ADD":
        creat_event = creat_review_and_point_count(request)
        if creat_event.is_valid():
            return Response(creat_event.data, status=status.HTTP_201_CREATED)
        return Response(creat_event.errors, status=status.HTTP_400_BAD_REQUEST)

    # update
    elif request.data['action'] == "MOD":
        update_event = update_review_and_point_count(request)
        if update_event.is_valid():
            return Response(update_event.data, status=status.HTTP_200_OK)
        return Response(update_event.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    elif request.data['action'] == "DELETE":
        delete = delete_review_and_point_count(request)
        return Response({"status": delete})


# user point 조회 api
class PointMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    lookup_field = "user_id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
