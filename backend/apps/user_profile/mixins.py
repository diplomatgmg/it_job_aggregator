from django.contrib.auth import get_user_model
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer

User = get_user_model()


class ProfileMixin:
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileAttributesMixin:
    attribute_model = None
    attribute_serializer = None
    attribute_field = None

    def get(self, request: Request) -> Response:
        profile = self.get_queryset().get(user=request.user)
        attributes = getattr(profile, self.attribute_field).all()
        serializer = self.attribute_serializer(attributes, many=True)
        return Response(serializer.data)

    def patch(self, request: Request) -> Response:
        user = request.user
        profile = Profile.objects.get(user=user)

        attributes_data = request.data or []
        attributes_ids = [attr.get("id") for attr in attributes_data]
        attributes = self.attribute_model.objects.filter(id__in=attributes_ids)

        getattr(profile, self.attribute_field).set(attributes)
        serializer = self.attribute_serializer(attributes, many=True)
        return Response(serializer.data)
