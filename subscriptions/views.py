from rest_framework import generics
from .serializers import SubscriptionSerializer
from .models import Subscriptions

class SubscriptionCreate(generics.ListCreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscriptions.objects.all()

class SubscriptionDelete(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscriptions.objects.all()

class SubscriptionUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscriptions.objects.all()

class SubscriptionView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    pagination_class = None
    queryset = Subscriptions.objects.all()