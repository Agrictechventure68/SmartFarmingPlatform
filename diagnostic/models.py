from django.db import models

class Diagnostic(models.Model):
    crop_name = models.CharField(max_length=100)
    disease_name = models.CharField(max_length=100)
    symptoms = models.TextField()
    solution = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.crop_name} - {self.disease_name}"
