from django.contrib import admin
from .models import Diagnostic

@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'region', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'symptoms', 'causes')
