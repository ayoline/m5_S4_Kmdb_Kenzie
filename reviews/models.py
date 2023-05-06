from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Recomendation(models.TextChoices):
    AVOID_WATCH = "Avoid Watch"
    SHOULD_WATCH = "Should Watch"
    MUST_WATCH = "Must Watch"
    NO_OPINION = "No Opinion"


class Review(models.Model):
    stars = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    review = models.TextField()
    spoilers = models.BooleanField(null=True, blank=True, default=False)

    recomendation = models.CharField(
        max_length=50,
        choices=Recomendation.choices,
        default=Recomendation.NO_OPINION,
    )

    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    critic = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="reviews",
    )
