from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = []
