from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
