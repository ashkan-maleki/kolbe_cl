from django.urls import path
from film import views


urlpatterns = [
    path('call', views.call),
]
