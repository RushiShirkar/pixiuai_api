from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255, unique=True)
    username = None
    password = models.CharField(max_length = 255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []