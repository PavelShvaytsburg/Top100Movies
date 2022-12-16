from rest_framework import generics
from django.db.models import Q

from .permissions import *
from .models import Movies
from .serializers import *


class MoviesAPIList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (ReadOnly, )

class WatchedMoviesAPIList(generics.ListAPIView):
    queryset = Movies.objects.filter(is_watched=True)
    serializer_class = MoviesSerializer
    permission_classes = (ReadOnly, )

class MoviesAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer2
    permission_classes = (UpdateRead, )

class TopMoviesAPIList(generics.ListAPIView):
    queryset = Movies.objects.all().exclude(place_in_top = None).order_by('place_in_top')
    serializer_class = MoviesSerializer
