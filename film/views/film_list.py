from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from film import repositories

repo = repositories.MovieRepository()


class FilmList(ListView):
    template_name = 'film/film_list.html'
    model = repo.get_model()




