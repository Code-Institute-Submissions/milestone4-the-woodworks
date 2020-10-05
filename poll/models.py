from django.db import models


class Poll(models.Model,):
    product_type = models.CharField(max_length=254, default='')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.product_type


class Voters(models.Model,):
    user_email = models.CharField(max_length=128, default='')
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.user_email
