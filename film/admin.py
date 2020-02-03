from django.contrib import admin
from film import models

# Register your models here.
admin.site.register(models.Movie)
admin.site.register(models.Series)
