from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from movies.views import *

def index(request):
    with open('movies/templates/index.html', 'r', encoding='utf8') as file:
        return HttpResponse(file.read())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', MoviesAPIList.as_view()),
    path('api/v1/movies/<int:pk>/', MoviesAPIDetailView.as_view()),
    path('api/v1/topmovies/', TopMoviesAPIList.as_view()),
    path('api/v1/watchedmovies/', WatchedMoviesAPIList.as_view()),

    path('', index)

]


#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
