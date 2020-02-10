from django.db import models


class BaseMovie(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(blank=True, null=True)
    imdb_id = models.CharField(max_length=25)
    # type = models.CharField(max_length=25)
    poster = models.CharField(max_length=300, blank=True)

    class Meta:
        abstract = True


class Movie(BaseMovie):
    pass
