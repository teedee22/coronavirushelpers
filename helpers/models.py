from django.db import models


class Helper(models.Model):
    postcode = models.TextField(null=False)
    link = models.TextField(null=False)
