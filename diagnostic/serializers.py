from rest_framework import serializers
from .models import Diagnostic

class DiagnosticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostic
        fields = '_all_'
