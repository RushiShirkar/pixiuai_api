from django.db import models
import uuid
from django.contrib.auth import get_user_model
from ideas.models import Idea
User = get_user_model()

# Create your models here.
class Subscriptions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    idea = models.ForeignKey(Idea, null=True, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)