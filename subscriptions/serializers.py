from rest_framework import serializers

from .models import Subscriptions

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = [
            'id', 'idea', 'user', 'status',
        ]