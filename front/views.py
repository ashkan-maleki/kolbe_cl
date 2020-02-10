from django.shortcuts import render, HttpResponse, reverse, redirect
from django.views import View


class Index(View):
    def get(self, request):
        return redirect('front-film:list')


index = Index.as_view()
