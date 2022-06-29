from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.fields.CharField(max_length=20, unique=True)
    password = models.fields.CharField(max_length=20)

    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='follow',
    )
