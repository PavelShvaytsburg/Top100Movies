from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Movies(models.Model):
    title = models.CharField(max_length=50)
    rate = models.DecimalField(
    max_digits = 2,
    decimal_places = 1,
    blank = True,
    null = True,
    validators = [
        MinValueValidator(1),
        MaxValueValidator(10)
    ]
    )
    image = models.ImageField()
    description = models.TextField()
    is_watched = models.BooleanField(default=False)
    place_in_top = models.IntegerField(
        blank = True,
        null = True,
        unique = True,
        validators = [
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    def __str__(self):
        return self.title
