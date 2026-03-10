from django.contrib import admin
from .models import Farmer

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
      list_filter = ('farm_type',)
search_fields = ('name', 'location', 'phone')  replace fields with actual ones from Farmer model
