from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    farm_type = models.CharField(max_length=100)
    registration_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
