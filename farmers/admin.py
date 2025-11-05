from django.contrib import admin
from .models import Farmer

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')  # ✅ replace fields with actual ones from Farmer model
