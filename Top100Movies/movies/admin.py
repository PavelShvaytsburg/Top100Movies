from django.contrib import admin
from .models import Movies


class MoviesAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'rate']

admin.site.register(Movies, MoviesAdmin)
