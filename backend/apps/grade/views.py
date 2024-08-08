from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics

from .models import Grade
from .serializers import GradeSerializer


@method_decorator(cache_page(600), name="dispatch")  # 10 Минут
class GradeListAPIView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
