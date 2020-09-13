from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=1024, default='')
    construction_time = models.DecimalField(max_digits=2, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
