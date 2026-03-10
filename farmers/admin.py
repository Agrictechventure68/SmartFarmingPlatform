from django.contrib import admin
from .models import Farmer


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'phone', 'farm_type')
    search_fields = ('name', 'location', 'phone')