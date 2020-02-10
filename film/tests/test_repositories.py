from django.test import TestCase
from base.repository import BaseRepository
from film import models, repositories


class RepositoryTest(TestCase):
    def test_movie_repository_class(self):
        repo = repositories.MovieRepository()
        self.assertEqual(type(models.Movie), type(repo.get_model()))

    def test_series_repository_class(self):
        repo = repositories.SeriesRepository()
        self.assertEqual(type(models.Series), type(repo.get_model()))


