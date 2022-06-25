from django.db.migrations import serializer
from rest_framework import generics, mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView

from mileage.api.serializers import ReviewSerializer, PointSerializer
from mileage.api.services import creat_review_and_point_count, update_review_and_point_count, \
    delete_review_and_point_count
from mileage.models import Review, Point


class EventAPIView(APIView):
    def post(self, request):
        if "type" == "REVIEW":
            # creat
            if "action" == "ADD":
                data = creat_review_and_point_count(request)
                return Response(data, status=status.HTTP_201_CREATED)
            # update
            elif "action" == "MOD":
                data = update_review_and_point_count(request)
                return Response(data, status=status.HTTP_200_OK)
            # delete
            elif "action" == "DELETE":
                delete_review_and_point_count(request)
                return Response(status=status.HTTP_200_OK)


# user point 조회 api
class PointMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    lookup_field = "user_id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
