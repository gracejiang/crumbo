from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class FoodPlace(models.Model):

    AMERICAN = 'AM'
    MEXICAN = 'MX'
    CHINESE = 'CH'
    KOREAN = 'KR'
    JAPANESE = 'JP'
    ITALIAN = 'IT'
    VIETNAMESE = "VN"
    INDIAN = 'IN'
    GREEK = 'GR'
    FRENCH = 'FR'
    MEDITERRANEAN = "MD"
    CAFE = 'CF'
    FAST_FOOD = 'FF'
    OTHER = 'OT'

    TYPE_CHOICES = [
        (AMERICAN, 'American'),
        (MEXICAN, 'Mexican'),
        (CHINESE, 'Chinese'),
        (KOREAN, 'Korean'),
        (JAPANESE, 'Japanese'),
        (ITALIAN, 'Italian'),
        (VIETNAMESE, 'Vietnamese'),
        (INDIAN, 'Indian'),
        (GREEK, 'Greek'),
        (FRENCH, 'French'),
        (MEDITERRANEAN, 'Mediterranean'),
        (CAFE, 'Cafe'),
        (FAST_FOOD, 'Fast Food'),
        (OTHER, 'Other')
    ]

    name = models.CharField(max_length=200, default='')
    type = models.CharField(
        max_length=200,
        choices=TYPE_CHOICES, default=AMERICAN)
    location = models.CharField(max_length=200, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, related_name="posts")
    rating = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(blank=True, default='')
    photos = models.TextField(blank=True, default='')
