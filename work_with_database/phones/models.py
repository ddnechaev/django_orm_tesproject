from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    price = models.IntegerField()
    image = models.CharField(max_length=1000)
    release_date = models.DateField()
    lte_exists = models.BooleanField()