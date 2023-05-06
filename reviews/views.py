from rest_framework import generics
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from .permissions import IsAdminOrCritic


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrCritic]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "movie_id"

    def get_queryset(self):
        movie_id = self.kwargs["movie_id"]
        return self.queryset.filter(movie=movie_id)

    def perform_create(self, serializer):
        movie_id = self.kwargs["movie_id"]
        reviews = self.queryset.filter(movie=movie_id, critic=self.request.user.id)

        if len(reviews):
            raise PermissionDenied("Review already exists.")

        serializer.save(movie_id=movie_id, critic_id=self.request.user.id)


class ReviewDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrCritic]

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_url_kwarg = "review_id"

    def get_queryset(self):
        movie_id = self.kwargs["movie_id"]
        review_id = self.kwargs["review_id"]
        review = self.queryset.filter(movie=movie_id, id=review_id).all()

        if len(review):
            return review

    def perform_destroy(self, instance):
        instance.delete()
