from django.db import models
‎
‎
‎class DiagnosticEntry(models.Model):
‎    enterprise = models.CharField(max_length=100)
‎    symptom = models.TextField()
‎    diagnosis = models.TextField()
‎    recommendation = models.TextField()
‎    created_at = models.DateTimeField(auto_now_add=True)
‎
‎    def __str__(self):
‎        return f"{self.enterprise} - {self.symptom}"
‎
‎
‎class DiagnosticHistory(models.Model):
‎    enterprise = models.CharField(max_length=100)
‎    symptom = models.TextField()
‎    result = models.TextField()
‎    created_at = models.DateTimeField(auto_now_add=True)
‎
‎    def __str__(self):
‎        return f"{self.enterprise} history"
‎