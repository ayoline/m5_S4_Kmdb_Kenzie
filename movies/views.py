from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminAndPostRoute, IsAdminAndDeleteRoute


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminAndPostRoute]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieUpdateView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminAndDeleteRoute]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_url_kwarg = "movie_id"
