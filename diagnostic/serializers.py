from rest_framework import serializers
from .models import DiagnosticEntry


class DiagnosticEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticEntry
        fields = '__all__'