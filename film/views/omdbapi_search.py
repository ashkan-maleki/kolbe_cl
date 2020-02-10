from django.shortcuts import render, HttpResponse, reverse, redirect
from django.views.generic import View


class OmdbApiSearchView(View):
    template_name = 'film/omdbapi_search.html'

    def get(self, request):
        return render(request, self.template_name)

# from django.http import HttpResponseRedirect
#   from django.shortcuts import render
#   from django.views.generic import View
#   from .forms import MyForm
#
#   class MyFormView(View):
#       form_class = MyForm
#       initial = {'key': 'value'}
#       template_name = 'form_template.html'
#
#       def get(self, request, *args, **kwargs):
#           form = self.form_class(initial=self.initial)
#           return render(request, self.template_name, {'form': form})
#
#       def post(self, request, *args, **kwargs):
#           form = self.form_class(request.POST)
#           if form.is_valid():
#               # <process form cleaned data>
#               return HttpResponseRedirect('/success/')
#           return render(request, self.template_name, {'form': form})
