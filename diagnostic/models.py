from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    For unified categories: crop, livestock, aquaculture
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class DiagnosticEntry(models.Model):
    """
    Master table for diseases/pests or health issues
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='entries')
    name = models.CharField(max_length=100)
    symptoms = models.TextField()
    causes = models.TextField(blank=True, null=True)
    treatment = models.TextField()
    preventive_measures = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class DiagnosticHistory(models.Model):
    """
    Tracks user diagnostics for crops, livestock, or aquaculture
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diagnostic_history')
    diagnostic_entry = models.ForeignKey(DiagnosticEntry, on_delete=models.SET_NULL, null=True)
symptoms_input = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.diagnostic_entry.name} ({self.timestamp.date()})"