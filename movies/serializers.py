from rest_framework import serializers
from genres.models import Genre
from genres.serializers import GenreSerializer
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "premiere",
            "duration",
            "classification",
            "synopsis",
            "genres",
        ]

    def create(self, validated_data: dict):
        genres_list = []
        genres = validated_data.pop("genres")

        for genre in genres:
            obj, _ = Genre.objects.get_or_create(**genre)
            genres_list.append(obj)

        movie_obj = Movie.objects.create(**validated_data)
        movie_obj.genres.set(genres_list)

        return movie_obj

    def update(self, instance: Movie, validated_data: dict):
        if "genres" in validated_data:
            instance.genres.clear()
            genres = validated_data.pop("genres")
            for genre in genres:
                obj, _ = Genre.objects.get_or_create(**genre)
                instance.genres.add(obj)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
