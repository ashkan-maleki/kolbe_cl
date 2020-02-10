from django.urls import path
from film import views


app_name = 'front-film'
urlpatterns = [
    path('call', views.call, name='call'),
    path('omdbapi-search', views.omdbapi_search, name='omdbapi-search'),
    path('', views.film_list, name='list'),
]
