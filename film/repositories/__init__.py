from film import models
from base.repository import BaseRepository


class MovieRepository(BaseRepository):
    class Meta:
        model = models.Movie


class SeriesRepository(BaseRepository):
    class Meta:
        model = models.Series
