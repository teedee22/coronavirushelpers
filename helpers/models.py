from django.db import models


class Helper(models.Model):
    postcodeFirst = models.TextField(null=False, max_length=4)
    postcodeSecond = models.TextField(null=False, max_length=3)
    link = models.TextField(null=False, max_length=900)
