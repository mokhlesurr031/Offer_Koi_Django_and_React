from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    username = models.CharField(unique=True, max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=155)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    contact = models.CharField(max_length=25)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

