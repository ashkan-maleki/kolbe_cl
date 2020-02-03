from django.db import models


class Series(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(blank=True, null=True)
    imbd_id = models.CharField(max_length=15)
    poster = models.CharField(max_length=300, blank=True)
