from django.contrib import admin
from .models import Diagnostic

@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('id', 'disease_name', 'symptoms')  # ✅ replace 'symptoms' if 
    