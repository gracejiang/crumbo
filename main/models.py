from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class FoodPlace(models.Model):

    class Type(models.TextChoices):
        AMERICAN = 'AM', _('American')
        MEXICAN = 'MX', _('Mexican')
        CHINESE = 'CH', _('Chinese')
        KOREAN = 'KR', _('Korean')
        JAPANESE = 'JP', _('Japanese')
        ITALIAN = 'IT', _('Italian')
        VIETNAMESE = "VN", _('Vietnamese')
        INDIAN = 'IN', _('Indian')
        GREEK = 'GR', _('Greek')
        FRENCH = 'FR', _('French')
        MEDITERRANEAN = "MD", _('Mediterranean')
        CAFE = 'CF', _('Cafe')
        FAST_FOOD = 'FF', _('Fast Food')

    name = models.CharField(max_length=200, default='')
    type = models.CharField(
        max_length=2, choices=Type.choices, default=Type.AMERICAN)
    location = models.CharField(max_length=200, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, related_name="posts")
    rating = models.IntegerField(
        default=3,
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.TextField(blank=True, default='')
    photos = models.JSONField()  # Takes in JSON array of URLs
