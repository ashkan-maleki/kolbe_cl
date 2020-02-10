from django.shortcuts import render
from django.http import HttpResponse
import datetime

import json
import requests

from film.views.film_list import FilmList
from film.views.omdbapi_search import OmdbApiSearchView

film_list = FilmList.as_view()
omdbapi_search = OmdbApiSearchView.as_view()


# Create your views here.
# http://www.omdbapi.com/?i=tt3896198&apikey=59e10d8


class Person(object):
    name = ''
    craft = ''

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __str__(self):
        return f'craft of {self.name} is {self.craft}'


def call(request):
    # request_url = "http://www.omdbapi.com/?i=tt3896198&apikey=59e10d8"
    request_url = "http://api.open-notify.org/astros.json"

    response = requests.get(request_url)

    status_code = response.status_code
    parsed_json = json.loads(response.content.decode('utf-8'))
    # output = str(parsed_json['people'])
    output = ''
    for p in parsed_json['people']:
        person = Person(**p)
        output += '<br>' + str(person)

    body = response.content
    body_str = '<br>' + str(body) + '<br>type:' + str(type(response.content))
    body_str += '<br>' + output + '<br>type:' + str(type(parsed_json))
    return HttpResponse(f'called! status code: {status_code}' + output)


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
