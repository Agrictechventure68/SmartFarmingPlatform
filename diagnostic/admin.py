from .models import Category, DiagnosticEntry, DiagnosticHistory

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(DiagnosticEntry)
class DiagnosticEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'region', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'symptoms', 'causes')

@admin.register(DiagnosticHistory)
class DiagnosticHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'diagnostic_entry', 'category', 'timestamp')
    list_filter = ('category',)
    search_fields = ('user__username',)