from rest_framework import serializers

from .models import Idea

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = [
            'id', 'name', 'crypto', 'risk', 'target', 'stoploss', 'created_at', 'user',
        ]