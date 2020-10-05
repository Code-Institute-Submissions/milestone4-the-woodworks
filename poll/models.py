from django.db import models


class Poll(models.Model,):
    product_type = models.CharField(max_length=254, default='')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.product_type

# class Has_voted(models.Model,):
#     email_adress