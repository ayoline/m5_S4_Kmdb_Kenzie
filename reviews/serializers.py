from rest_framework import serializers
from accounts.serializers import CriticSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "recomendation",
            "movie_id",
            "critic",
        ]

        read_only_fields = ["movie_id"]
