from rest_framework import viewsets
from .models import Diagnostic
from .serializers import DiagnosticSerializer

class DiagnosticViewSet(viewsets.ModelViewSet):
    queryset = Diagnostic.objects.all()
    serializer_class = DiagnosticSerializer