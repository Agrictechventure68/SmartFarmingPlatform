from django.db import models

class Diagnostic(models.Model):
    CATEGORY_CHOICES = [
        ('crop', 'Crop'),
        ('livestock', 'Livestock'),
        ('aquaculture', 'Aquaculture'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    symptoms = models.TextField()
    causes = models.TextField()
    treatment = models.TextField()
    preventive_measures = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"