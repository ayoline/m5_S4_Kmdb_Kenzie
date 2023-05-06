from django.urls import path
from .views import MovieView, MovieUpdateView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieUpdateView.as_view()),
]
