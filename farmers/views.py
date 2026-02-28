from rest_framework import viewsets
from .models import Farmer
from .serializers import FarmerSerializer

from rest_framework import filters

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all().order_by('-registration_date')
    serializer_class = FarmerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'location', 'farm_type']
