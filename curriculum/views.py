from rest_framework import viewsets
from .models import Curriculum
from .serializers import CurriculumSerializer

from rest_framework import filters

class CurriculumViewSet(viewsets.ModelViewSet):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'level']
    ordering_fields = ['created_at', 'title']
