from django.db import models

class Curriculum(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title
