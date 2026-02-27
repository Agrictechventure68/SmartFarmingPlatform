from rest_framework import serializers
from .models import Diagnostic

class DiagnosticEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticEntry
        fields = '__all__'
