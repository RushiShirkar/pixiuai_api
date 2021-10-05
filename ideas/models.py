from django.db import models
import uuid
from django.contrib.auth import get_user_model
User = get_user_model()

class Idea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(blank=True, null=True)
    crypto = models.CharField(max_length=255, blank=True, null=True)
    risk = models.CharField(max_length=255, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    stoploss = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
