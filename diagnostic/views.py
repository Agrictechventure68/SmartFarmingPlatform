from rest_framework import viewsets, filters
from .models import DiagnosticEntry
from .serializers import DiagnosticEntrySerializer


class DiagnosticViewSet(viewsets.ModelViewSet):
    queryset = DiagnosticEntry.objects.all().order_by('-created_at')
    serializer_class = DiagnosticEntrySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'symptoms', 'causes']
    ordering_fields = ['created_at', 'name']