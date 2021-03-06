from django.db import models


class Product(models.Model):
    """
    This model will store all products with name,
    description, construction time, price and image name.
    """
    name = models.CharField(max_length=254, default='')
    description = models.CharField(max_length=1024, default='')
    construction_time = models.DecimalField(max_digits=2, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
