from django.db import models
from django.utils import timezone


class Shops(models.Model):
    name = models.CharField(unique=True, max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.name
