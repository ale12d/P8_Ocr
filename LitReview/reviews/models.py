from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Ticket(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=2048, blank=True)
    images = models.ImageField(upload_to=settings.MEDIA_ROOT,
                               blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)
    headline = models.fields.CharField(max_length=128)
    body = models.fields.CharField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)])
