from rest_framework import generics, mixins

from mileage.api.serializers import ReviewSerializer, PointSerializer
from mileage.models import Review, Point


class EventGeneric(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        if "action" == "DELETE":
            pass

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if "action" == "ADD":
            pass
        if "action" == "MOD":
            pass

        return self.create(request, *args, **kwargs)


# user point 조회 api
class PointMixins(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    lookup_field = "user_id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
